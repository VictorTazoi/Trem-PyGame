import pygame as pg

pg.init()

# Resolução de tela
tela_x = 1260
tela_y = 700

# Criação de tela
tela = pg.display.set_mode((tela_x, tela_y))

# Ajuste de altura
alt_tela = 60  # Ajusta a altura do trem (apenas para desenvolvimento e testes)

# Configuração de raio das rodas
ext_r = 50  # Raio interno da roda
ext_g = 50
ext_b = 50
inter_r = 255  # Raio externo da roda
inter_g = 255
inter_b = 255

# Variáveis de posição de cada estaca do trilho
x0_mad = 0
x1_mad = 60
x2_mad = 120
x3_mad = 180
x4_mad = 240
x5_mad = 300
x6_mad = 360
x7_mad = 420
x8_mad = 480
x9_mad = 540
x10_mad = 600
x11_mad = 660
x12_mad = 720
x13_mad = 780
x14_mad = 840
x15_mad = 900
x16_mad = 960
x17_mad = 1020
x18_mad = 1080
x19_mad = 1140
x20_mad = 1200

y_mad = 595  # Altura das estacas
vx_mad = 0.1  # Velocidade das estacas (Serve como timer para manter sincronia nas ações)

# tempo
dia = (0, 160, 255)  # Define a cor da esfera que desliza a cor do dia
noite = (10, 0, 0)  # Define a cor da esfera que desliza a cor da noite
tempo = 11  # Esqueci para que serve essa variável, mas recomendo não mexer, pois alterei e bagunçou tudo :)
raio_tempo = 0  # Define o raio inicial do circulo usado para deslizar a cor do dia e noite
vraio_tempo = 0.9  # Define velocidade do circulo usado para deslizar a cor do dia e noite
cor_fundo = 11  # Serve para declarar a cor de fundo, 11 é um numero aleatorio, pois o valor é atribuido depois

# Lua e Sol
cor_lua = (150, 150, 255)  # Cor da Lua
cor_sol = (255, 255, 150)  # Cor do Sol
cor_ls = cor_lua  # Inicia com a cor da Lua
r_ls = 50  # Define o raio da Lua e do Sol
x_ls = tela_x  # Posição X de início
y_ls = 100  # Posição Y de início
v_ls = 0.1  # Velocidade de deslizamento da Lua e do Sol
estagio = 3  # Estagios servem para definir quando o elemento aparece e some. (1 para aparecer, 2 para sumir. Desconsiderar o 3)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()

    # Apagar a tela
    tela.fill(cor_fundo)

    # Montagem de cena

    # Define o tempo, que é a esfera que desliza a cor do dia e noite
    pg.draw.circle(tela, (tempo), (tela_x, 0), raio_tempo)

    # Define a Lua e o Sol
    pg.draw.circle(tela, (cor_ls), (x_ls, y_ls), r_ls)

    # Grama
    pg.draw.polygon(tela, (34, 177, 76), [(0, 610), (tela_x, 610), (tela_x, tela_y), (0, tela_y)])

    # Estrutura do Trem
    pg.draw.rect(tela, (150, 150, 150), (150, 330 + alt_tela, 200, 170))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (100, 100, 100), (350, 470 + alt_tela, 30, 20))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (150, 150, 150), (380, 250 + alt_tela, 150, 250))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (100, 100, 100), (350, 210 + alt_tela, 210, 40))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (0, 0, 0), (410, 280 + alt_tela, 90, 90))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (120, 120, 120), (530, 350 + alt_tela, 250, 150))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.polygon(tela, (50, 50, 50), [(780, 370 + alt_tela), (780, 480 + alt_tela), (860, 480 + alt_tela)])
    pg.draw.rect(tela, (150, 150, 150), (700, 300 + alt_tela, 50, 50))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.polygon(tela, (50, 50, 50), [(685, 300 + alt_tela), (725, 260 + alt_tela), (765, 300 + alt_tela)])

    # Rodas do Trem
    pg.draw.circle(tela, ((ext_r, ext_g, ext_b)), (200, 500 + alt_tela), 40)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((inter_r, inter_g, inter_b)), (200, 500 + alt_tela), 20)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((ext_r, ext_g, ext_b)), (300, 500 + alt_tela), 40)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((inter_r, inter_g, inter_b)), (300, 500 + alt_tela), 20)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((ext_r, ext_g, ext_b)), (430, 500 + alt_tela), 40)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((inter_r, inter_g, inter_b)), (430, 500 + alt_tela), 20)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((ext_r, ext_g, ext_b)), (550, 500 + alt_tela), 40)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((inter_r, inter_g, inter_b)), (550, 500 + alt_tela), 20)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((ext_r, ext_g, ext_b)), (750, 500 + alt_tela), 40)  # ((x_pos, y_pos), raio)
    pg.draw.circle(tela, ((inter_r, inter_g, inter_b)), (750, 500 + alt_tela), 20)  # ((x_pos, y_pos), raio)

    # Trilho de aço
    pg.draw.rect(tela, (120, 120, 120), (0, 600, tela_x, 10))  # (x_pos, y_pos, tam_x, tam_y)

    # EEstacas do trilho (tabuas)
    pg.draw.rect(tela, (92, 64, 51), (x0_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x1_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x2_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x3_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x4_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x5_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x6_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x7_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x8_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x9_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x10_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x11_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x12_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x13_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x14_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x15_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x16_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x17_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x18_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x19_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)
    pg.draw.rect(tela, (92, 64, 51), (x20_mad, y_mad, 30, 15))  # (x_pos, y_pos, tam_x, tam_y)

    # Atualizar o frame
    pg.display.flip()

    # Movimento das estacas dos trilhos (tabuas)
    x0_mad += -vx_mad
    x1_mad += -vx_mad
    x2_mad += -vx_mad
    x3_mad += -vx_mad
    x4_mad += -vx_mad
    x5_mad += -vx_mad
    x6_mad += -vx_mad
    x7_mad += -vx_mad
    x8_mad += -vx_mad
    x9_mad += -vx_mad
    x10_mad += -vx_mad
    x11_mad += -vx_mad
    x12_mad += -vx_mad
    x13_mad += -vx_mad
    x14_mad += -vx_mad
    x15_mad += -vx_mad
    x16_mad += -vx_mad
    x17_mad += -vx_mad
    x18_mad += -vx_mad
    x19_mad += -vx_mad
    x20_mad += -vx_mad

    # Controle de expansão do tempo, o qual fará a esfera aumentar o raio representando a cor do dia
    raio_tempo += vraio_tempo

    # Estagios do Sol e da Lua
    if estagio == 1:  # Estagio 1, aparecer
        x_ls += -v_ls
    elif estagio == 0:  # Estagio 2, sumir
        x_ls += v_ls
    elif estagio == 2:  # Estagio 3, parar
        x_ls = x_ls

    # Controle de colisão das estacas (tabuas) dos trilhos
    # Caso a estaca chegue no X = 0, a mesma é jogada para o ponto X limite da tela
    if x0_mad < 0:
        x0_mad = tela_x
        raio_tempo = 0  # Reinicia o tamanho do raio
        x_ls = tela_x + r_ls  # Posiciona o raio para o início do canto direito da tela
        cor_fundo = dia  # Define a cor de fundo
        tempo = noite  # Define o tempo
        estagio = 1  # Define o estágio de aparecimento do elemento
        cor_ls = cor_lua  # Define a cor do elemento, no caso, define a cor da Lua
    elif x1_mad < 0:
        x1_mad = tela_x
    elif x2_mad < 0:
        x2_mad = tela_x
    elif x3_mad < 0:
        x3_mad = tela_x
    elif x4_mad < 0:
        x4_mad = tela_x
        estagio = 0  # Define o estágio de desaparecimento do elemento
    elif x5_mad < 0:
        x5_mad = tela_x
    elif x6_mad < 0:
        x6_mad = tela_x
    elif x7_mad < 0:
        x7_mad = tela_x
    elif x8_mad < 0:
        x8_mad = tela_x
    elif x9_mad < 0:
        x9_mad = tela_x
    elif x10_mad < 0:
        x10_mad = tela_x
        raio_tempo = 0  # Reinicia o tamanho do raio
        x_ls = tela_x + r_ls  # Posiciona o raio para o início do canto direito da tela
        cor_fundo = noite  # Define a cor de fundo
        tempo = dia  # Define o tempo
        estagio = 1  # Define o estágio de aparecimento do elemento
        cor_ls = cor_sol  # Define a cor do elemento, no caso, define a cor do Sol
    elif x11_mad < 0:
        x11_mad = tela_x
    elif x12_mad < 0:
        x12_mad = tela_x
    elif x13_mad < 0:
        x13_mad = tela_x
    elif x14_mad < 0:
        x14_mad = tela_x
        estagio = 0  # Define o estágio de desaparecimento do elemento
    elif x15_mad < 0:
        x15_mad = tela_x
    elif x16_mad < 0:
        x16_mad = tela_x
    elif x17_mad < 0:
        x17_mad = tela_x
    elif x18_mad < 0:
        x18_mad = tela_x
    elif x19_mad < 0:
        x19_mad = tela_x
    elif x20_mad < 0:
        x20_mad = tela_x
        