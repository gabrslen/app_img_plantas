import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Caminho da imagem inicial
image_path = None
original_img = None

# Configurações iniciais
params = {
    'gradient_ksize': None,  # Tamanho do kernel para cálculo do gradiente
    'threshold_value': None,  # Valor de limiar para binarização
    'markers_ksize': None,  # Tamanho do kernel para cálculo dos marcadores
    'contour_thickness': None, # Espessura em px dos contornos adicionados
    'epsilon': None, # Precisão dos contornos
    'contour_color': None, # Cor dos contornos, cód RGB
    'numero_clusters': None, # Quantidade de Clusters considerados
    'contraste': None,
    'brilho': None
    }

def carregar_imagem(original_img, largura_padrao=None):

    image = tf.io.read_file(original_img)
    image = tf.image.decode_image(image, channels=3)
    
    imagem_numpy = image.numpy()
    altura, largura, _ = imagem_numpy.shape

    proporcao = largura_padrao / largura
    nova_largura = largura_padrao
    nova_altura = int(altura * proporcao)
    imagem_redimensionada = cv2.resize(imagem_numpy, (nova_largura, nova_altura))

    cv2.imwrite('imagem_redimensionada.jpg', cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2RGB))

    return imagem_redimensionada

def converter_tons_cinza(image_path, contraste=None, brilho=None):
    
    contraste = params['contraste']
    brilho = params['brilho']
    
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_image_contrast = cv2.convertScaleAbs(gray_image, alpha=contraste, beta=brilho)

    return gray_image_contrast

def show_gradient_magnitude(image_path, contraste=None, brilho=None):
    gradient_ksize = params['gradient_ksize']
    gray_image = converter_tons_cinza(image_path, contraste, brilho)

    gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=gradient_ksize)
    gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=gradient_ksize)

    gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)
    gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)
    
    return gradient_magnitude

def watersheed_image(image_path, params):

    gradient_magnitude = show_gradient_magnitude(image_path, params['gradient_ksize'])
    gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

    scaled_image = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite('imagem_gradiente.jpg', scaled_image)
    image_color = cv2.cvtColor(gradient_magnitude, cv2.COLOR_GRAY2BGR)

    _, markers = cv2.threshold(gradient_magnitude, params['threshold_value'], 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    markers = cv2.connectedComponents(markers, params['markers_ksize'])[1]

    result = cv2.watershed(image_color, markers)

    segmented_image = np.copy(image_color)
    for label in np.unique(result):
        if label == -1:
            continue
        mask = np.zeros_like(result, dtype=np.uint8)
        mask[result == label] = 255
        color = np.random.randint(0, 255, size=(3,))
        segmented_image[mask > 0] = color
    
    cv2.imwrite('imagem_segmentada.jpg', cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
