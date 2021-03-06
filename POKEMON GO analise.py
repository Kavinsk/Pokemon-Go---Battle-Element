# ELEMENTOS
vFogo = ("Fogo, Terrestre, Gelo, Inseto, Metálico")
dFogo = ("Água, Terrestre, Pedra, Dragão")
vAgua = ("Fogo, Gelo, Água, Metálico, Terrestre, Pedra")
dAgua = ("Planta, Elétrico, Dragão")
vGrama = ("Água, Planta, Elétrico, Terrestre, Pedra")
dGrama = ("Fogo, venenoso, Inseto, Voador, Gelo, Dragão, Metálico")
vEletrico = ("Água, Voador")
dEletrico = ("Terrestre, Planta, Dragão")
vTerrestre = ("Venenoso, Pedra, Fogo, Elétrico, Metálico")
dTerrestre = ("Água, Grama, Gelo, Inseto")
vNormal = ("Fantasma")
dNormal = ("Lutador, Pedra, Metálico e Fantasma")
vPedra = ("Fogo, Gelo, Voador, Inseto, Normal, Venenoso")
dPedra = ("Água, Planta, Lutador, Terrestre, Metálico")
vVoador = ("Grama, Lutador, Inseto, Terrestre")
dVoador = ("Elétrico, Gelo, Pedra, Metálico")
vVenenoso = ("Fada, Planta, Inseto, Lutador")
dVenenoso = ("Terrestre, Psíquicos")
vInseto = ("Planta, Psíquico, Noturno, Terrestre, Lutador")
dInseto = ("Fogo, Voador, Pedra, Lutador, Venenoso, Fantasma, metálico")
vNoturno = ("Psíquico, Fantasma")
dNoturno = ("Lutador, Inseto, Fada")
vFantasma = ("Venenoso, Inseto, Psíquico, Fantasma, Normal, Lutador")
dFantasma = ("Noturno, Fantasma, Normal")
vPsiquico = ("Lutador, Venenoso")
dPsiquico = ("Inseto, Fantasma, Noturno")
vDragao = ("Água, Fogo, Planta, Elétrico, Dragão")
dDragao = ("Dragão, Gelo, Metálico e Fada")
vMetalico = ("Fada, Gelo, Pedra, Planta, Inseto, Dragão, Voador, Normal, Psíquico, Metálico")
dMetalico = ("Fogo, Lutador, Terrestre, Água, Elétrico")
vGelo = ("Planta, Terrestre, Voador, Dragão")
dGelo = ("Fogo, Lutador, Pedra, Metálico, Água")
vLutador = ("Inseto, Pedra, Noturno, Normal, Gelo, Metálico")
dLutador = ("Fada, Voador, Psíquico, Venenoso, Inseto, Fantasma")
vFada = ("Noturno, Lutador, Inseto, Dragão")
dFada = ("Venenoso, Metálico, Fogo")

# INFO
van = "Vantagem: "
des =  "Desvantagem: "

# POKEMON
Abra = van+vPsiquico, des+dPsiquico
Absol = van+vNoturno, des+dNoturno
Aerodactyl = van+vPedra+", "+vVoador,des+dPedra+dVoador
Aggron = van+vMetalico+", "+vPedra,des+dMetalico+", "+dPedra
Alakazam = van+vPsiquico, des+dPsiquico
Arcanine = van+vFogo, des+dFogo
Articuno = van+vGelo, des+dGelo
Bayleef = van+vGrama, des+dGrama
Blissey = van+vNormal, des+dNormal
Bulbasaur = van+vGrama+", "+vVenenoso, des+dGrama+", "+dVenenoso
Charizard = van+vFogo+", "+vVoador, des+dFogo+", "+dVoador
Charmeleon = van+vFogo, des+dFogo
Charmander = van+vFogo, des+dFogo
Clefairy = van+vFada, des+dFada
Cloyster = van+vAgua+", "+vGelo, des+dAgua+", "+dGelo
Croconaw = van+vAgua, des+dAgua
Cubone = van+vTerrestre, des+dTerrestre
Dragonnair = van+vDragao, des+dDragao
Dragonite = van+vDragao+", "+vVoador, des+dDragao+", "+dVoador
Electabuzz = van+vEletrico, des+dEletrico
Entei = van+vFogo, des+dFogo
Espeon = van+vPsiquico, des+dPsiquico
Exeggutor = van+vGrama+", "+vPsiquico, des+dGrama+", "+dPsiquico
Feraligatr = van+vAgua, des+dAgua
Flareon = van+vFogo, des+dFogo
Gardevoir = van+vPsiquico+", "+vFada, des+dPsiquico+", "+dFada
Gastly = van+vFantasma, des+dFantasma
Groudon = van+vTerrestre, des+dTerrestre
Grovyle = van+vGrama, des+dGrama
Gyarados = van+vAgua+", "+vVoador, des+dAgua+", "+dVoador
Heracross = van+vInseto+", "+vLutador, des+dInseto+", "+dLutador
Hitmonlee = van+vLutador, des+dLutador
Houndoom = van+vNoturno+", "+vFogo, des+dNoturno+", "+dFogo
Jolteon = van+vEletrico, des+dEletrico
