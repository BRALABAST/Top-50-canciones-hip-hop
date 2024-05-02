def crear_lista(iterable, longitud_maxima=None):
    resultado = []
    for elemento in iterable:
        resultado.append(elemento)
        if longitud_maxima and len(resultado) >= longitud_maxima:
            resultado = tuple(resultado)
            break
    return resultado

# 50 mejores canciones de hip hop
canciones_hip_hop = [
    "Juicy - The Notorious B.I.G. (1994)",  # Clásico atemporal del rap east coast.
    "N.Y. State of Mind - Nas (1994)",  # Retrato crudo de la vida en las calles de Nueva York.
    "C.R.E.A.M. - Wu-Tang Clan (1993)",  # Himno del Wu-Tang Clan sobre el dinero y el poder.
    "Nuthin' but a 'G' Thang - Dr. Dre ft. Snoop Doggy Dogg (1992)",  # Éxito que popularizó el sonido G-funk.
    "Mind Playing Tricks on Me - Geto Boys (1991)",  # Canción oscura y psicodélica sobre la paranoia.
    "Shook Ones, Pt. II - Mobb Deep (1995)",  # Clásico del rap hardcore de Nueva York.
    "The Message - Grandmaster Flash and the Furious Five (1982)",  # Canción pionera que retrata la vida en los guetos.
    "Straight Outta Compton - N.W.A. (1988)",  # Himno del gangsta rap que desafió la censura.
    "Dear Mama - 2Pac (1995)",  # Emotiva oda de 2Pac a su madre.
    "Hypnotize - The Notorious B.I.G. (1997)",  # Éxito de Biggie con un sample pegadizo.
    "93' til Infinity - Souls of Mischief (1993)",  # Joya del rap alternativo de los 90.
    "Slick Rick - La Di Da Di (1985)",  # Clásico del rap narrativo contado por Slick Rick.
    "Passin' Me By - The Pharcyde (1992)",  # Canción innovadora del rap alternativo de Los Ángeles.
    "The Choice Is Yours (Revisited) - Black Sheep (1991)",  # Éxito del rap alternativo de comienzos de los 90.
    "Electric Relaxation - A Tribe Called Quest (1993)",  # Canción relajada y melódica de Tribe Called Quest.
    "Rapper's Delight - The Sugarhill Gang (1979)",  # Primer éxito del hip hop que lo popularizó.
    "Respiration - Black Star (1998)",  # Colaboración entre Mos Def y Talib Kweli.
    "6 'N' the Mornin' - Ice-T (1986)",  # Clásico del rap crudo y callejero de Ice-T.
    "Follow the Leader - Eric B. & Rakim (1988)",  # Canción innovadora que definió el sonido del rap consciente.
    "Mobb Deep - Survival of the Fittest (1995)"  # Clásico del rap hardcore de Nueva York.
]

# Crear una lista con las 20 primeras canciones
top_20_canciones = crear_lista(canciones_hip_hop, longitud_maxima=20)
print("Top 20 canciones de hip hop:")
print(top_20_canciones)

# Crear una tupla con todas las canciones
todas_las_canciones = crear_lista(canciones_hip_hop)
print("\nTodas las canciones (como tupla):")
print(todas_las_canciones)