map_romania = dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Zerind=dict(Arad=75, Oradea=71),
    Timisoara=dict(Arad=118, Lugoj=111),
    Mehadia=dict(Lugoj=70, Drobeta=75),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75, Craiova=120),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99, Bucharest=211),
    Hirsova=dict(Urziceni=98, Eforie=86),
    Vaslui=dict(Iasi=92, Urziceni=142),
    Iasi=dict(Vaslui=92, Neamt=87),
    Neamt=dict(Iasi=87),
    Giurgiu=dict(Bucharest=90),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97, Craiova=138, Bucharest=101),
    Sibiu=dict(Oradea=151, Arad=140, Rimnicu=80, Fagaras=90),
    Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
    Urziceni=dict(Vaslui=142, Bucharest=85, Hirsova=98))

vaccum_world = dict(
    ESS=dict(ELS="Aspirar", DSS="Direita"),
    ELS=dict(DLS="Direita"),
    ESL=dict(ELL="Aspirar", DSL="Direita"),
    ELL=dict(DLL="Direita"),
    DSS=dict(DSL="Aspirar", ESS="Esquerda"),
    DLS=dict(DLL="Aspirar", ELS="Esquerda"),
    DSL=dict(ESL="Esquerda"),
    DLL=dict(ELL="Esquerda")
)

# Distância de linha reta heurística
HSLD = dict(
    Arad=366,
    Bucharest=0,
    Craiova=160,
    Drobeta=242,
    Eforie=161,
    Fagaras=176,
    Giurgiu=77,
    Hirsova=151,
    Iasi=226,
    Lugoj=244,
    Mehadia=241,
    Neamt=234,
    Oradea=380,
    Pitesti=100,
    Rimnicu=193,
    Sibiu=253,
    Timisoara=329,
    Urziceni=80,
    Vaslui=199,
    Zerind=374
)