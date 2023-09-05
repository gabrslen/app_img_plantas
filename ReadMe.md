Bem vindo à apresentação das funcionalidades do projeto!

Vamos começar com algumas informações de configuração básica:

Linguagem utilizada:
Python 3.11.4

instale o python marcando a opção:
add Python.exe to PATH

Com o python instalado escolha o diretório que irá manter o projeto e crie o
ambiente virtual para trabalhar dentro dele através do comando:

python -m venv visao

OBS: uma pasta denominada "visao" será criada automaticamente dentro do 
diretório atual do projeto. Certifique-se de ativar o ambiente virtual
através do arquivo:

visao\Scripts\Activate.ps1

Bibliotecas necessárias para o funcionamento da ferramenta:

- pip install tensorflow

- pip install opencv-python

- pip install matplotlib

- pip install numpy



para um detalhamento mais apurado dos passos para instalação do tensorflow:
https://www.tensorflow.org/install?hl=pt-br

-----------------------------------------------------------------------------

A proposta inicial é fornecer os dois filtros demonstrados no arquivo:

\img\amostras\FiltrosReferencia.jpg

... nesta imagens observamos a apresentação das amostras processadas:

1 - Exibe a imagem com o filtro gradiente para destacar os contornos.

2 - aplica o filtro de watershed para segmentar a imagem em cores opacas.

com uma imagem de regiões bem definidas e de cores destacadas umas das outras
pode-se criar máscaras para recorte das imagens considerando suas áreas.

inicialmente teremos o arquivo app.py como interface.
posteriormente será desenvolvida uma GUI para facilitar o contato.

no arquivo app.py você encontrará os seguintes elementos:

------------------------------------------------------------------------------
------------------------------------------------------------------------------

import modules.funcoes as app

original_img = r'img\amostras\AmostraAleatoria.jpg'

image_path = r'imagem_redimensionada.jpg'

params = app.params = {
        'gradient_ksize': 1,
        'threshold_value': 20,
        'markers_ksize': 4,
        'contraste': 1.4,
        'brilho': 0.0
        }

#gradiente = app.show_gradient_magnitude(image_path,contraste=None,brilho=None)

#segmentada = app.watersheed_image(image_path,params)

imagem = app.carregar_imagem(original_img, largura_padrao=680)

------------------------------------------------------------------------------
------------------------------------------------------------------------------

O link da imagem original deve se colocado na variável original_img

...cada numeral no dicionario params pode ser alterado para diferentes outputs.

agora com a imagem original carregada, deve executar primeiramente a função:
app.carregar_imagem(original_img, largura_padrao=680)

no campo largura_padrão: pode-se optar por outras larguras de imagem, em um
contexto com diferentes fontes de imagens, com tamanhos diferentes, vamos
usar uma largura padrão para não sobrecarregar com imagens pesadas o sistema
ajudando para o nível de qualidade que se precisa.

depois de executar o comando desta função o sistema gerará na raiz um novo
arquivo: imagem_redimensionada.jpg

-------------------------------------------------------------------------------

com a imagem_redimensionada na raiz, voce pode remover os # das duas outras
funções:

app.show_gradient_magnitude(image_path,contraste=None,brilho=None)

app.watersheed_image(image_path,params)

IMPORTANTE:
Adicione um # antes da função de carregar imagem quando já estiver no segundo
passo.

#imagem = app.carregar_imagem(original_img, largura_padrao=680)

--------------------------------------------------------------------------------

As imagens serão salvas na raiz do projeto por enquanto, alguns exemplos já
executados podem ser encontrados no diretório:

img\outputs

dentro do projeto.

Em breve virão atualizações de interface e funções...
