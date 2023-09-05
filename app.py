import modules.funcoes as app

original_img = r'img\amostras\AmostraAleatoria.jpg'
image_path = r'imagem_redimensionada.jpg'

params = app.params = {
        'gradient_ksize': 1,  # Tamanho do kernel para cálculo do gradiente
        'threshold_value': 20,  # Valor de limiar para binarização
        'markers_ksize': 4,  # Tamanho do kernel para cálculo dos marcadores
        'contraste': 1.4,
        'brilho': 0.0
        }

gradiente = app.show_gradient_magnitude(image_path,contraste=None,brilho=None)
segmentada = app.watersheed_image(image_path,params)
#imagem = app.carregar_imagem(original_img, largura_padrao=680)


'''
# Usar para a amostra img\amostras\AmostraReferencia.jpg:

params = app.params = {
        'gradient_ksize': 1,  # Tamanho do kernel para cálculo do gradiente
        'threshold_value': 10,  # Valor de limiar para binarização
        'markers_ksize': 1,  # Tamanho do kernel para cálculo dos marcadores
        'contraste': 1.6,
        'brilho': 30.0
        }
'''