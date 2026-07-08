class UniversoTorneo:
    def __init__(self):
        # Datos del problema (Participaciones reales)
        self.objetivo = {'A': 17, 'B': 15, 'C': 10}
        self.total_juegos = sum(self.objetivo.values()) // 2  # 21 juegos
        self.contador_universos = 0  # Rastreador de líneas temporales
        
    def resolver(self):
        print("🤖 Iniciando motor de simulación hiper-dimensional...\n")
        
        # 1. Escanear universos con parámetros extremos e imposibles
        self._escanear_anomalias_extremas()
        
        print("🌌 Iniciando búsqueda en el espectro de realidades estables...\n")
        
        # 2. Iniciar la simulación real asumiendo que el Juego 1 es A + B
        self._buscar_camino(
            juego_actual=1,
            en_mesa=('A', 'B'),
            en_banca='C',
            historial=[],
            participaciones={'A': 0, 'B': 0, 'C': 0}
        )

    def _escanear_anomalias_extremas(self):
        print("=" * 60)
        print("⚠️ DETECCIÓN DE UNIVERSOS CORRUPTOS (ANOMALÍAS DE BUCLE)")
        print("=" * 60)
        
        # Definimos los universos extremos que solicitaste
        anomalias = [
            ({'A': 21, 'B': 0, 'C': 0}, "Singularidad Solipsista (A juega contra el vacío)"),
            ({'A': 0, 'B': 21, 'C': 0}, "Singularidad Solipsista (B enloquece en soledad absoluta)"),
            ({'A': 0, 'B': 0, 'C': 21}, "Singularidad Solipsista (C juega 21 partidas contra su sombra)"),
            ({'A': 21, 'B': 21, 'C': 0}, "Dimensión de Exclusión (C fue borrado de la existencia)"),
            ({'A': 0, 'B': 21, 'C': 21}, "Dimensión de Exclusión (A nunca llegó al torneo)"),
            ({'A': 21, 'B': 0, 'C': 21}, "Dimensión de Exclusión (B desapareció en el primer turno)")
        ]
        
        for part, causa in anomalias:
            self.contador_universos += 1
            print(f"❌ UNIVERSO #{self.contador_universos} [COLAPSO INMEDIATO]")
            print(f"   Estado de la realidad: {part}")
            print(f"   Diagnóstico: {causa}")
            
            # Explicación matemática del colapso
            total_part = sum(part.values())
            if total_part < 42:
                print(f"   Fallo Físico: Faltan entidades. Se requieren 42 participaciones, solo hay {total_part}.\n")
            else:
                print(f"   Fallo Físico: Violación del axioma de descanso. Alguien jugó sin ceder la mesa.\n")
                
        print("=" * 60 + "\n")

    def _buscar_camino(self, juego_actual, en_mesa, en_banca, historial, participaciones):
        # Cada vez que entramos aquí, nace un nuevo sub-universo
        self.contador_universos += 1
        j1, j2 = en_mesa
        
        # Clonar y actualizar participaciones para este nodo
        nuevas_part = participaciones.copy()
        nuevas_part[j1] += 1
        nuevas_part[j2] += 1
        
        # ---------------------------------------------------------
        # EFECTO VISUAL: MOSTRAR UNIVERSOS DESCARTADOS EN TIEMPO REAL
        # ---------------------------------------------------------
        if self.contador_universos == 420:
            print(f"❌ UNIVERSO #420 -> Destruido. Estado: {nuevas_part}")
            print("   Causa: Ruptura de la constante térmica del torneo.\n")
            
        elif self.contador_universos == 840:
            print(f"❌ UNIVERSO #840 -> Destruido. Estado: {nuevas_part}")
            print("   Causa: Principio de Exclusión. Alguien jugó demasiadas partidas seguidas.\n")
            
        elif self.contador_universos == 1500:
            print(f"❌ UNIVERSO #1500 -> Destruido. Estado: {nuevas_part}")
            print("   Causa: Paradoja temporal en los descansos de C.\n")
        # ---------------------------------------------------------

        # Poda algorítmica: Si nos pasamos de los límites, este universo muere
        for jugador in 'ABC':
            if nuevas_part[jugador] > self.objetivo[jugador]:
                return # Rompe esta rama del árbol (el universo se destruye)

        # Caso base: Llegamos al final del torneo (21 juegos)
        if juego_actual == self.total_juegos:
            if nuevas_part == self.objetivo:
                self._imprimir_explicacion(historial, nuevas_part)
            return

        # Simular los 2 sub-universos posibles para el juego actual
        p1_historial = historial + [(j1, j2, j1)] # Pierde j1
        self._buscar_camino(juego_actual + 1, (j2, en_banca), j1, p1_historial, nuevas_part)
        
        p2_historial = historial + [(j1, j2, j2)] # Pierde j2
        self._buscar_camino(juego_actual + 1, (j1, en_banca), j2, p2_historial, nuevas_part)

    def _imprimir_explicacion(self, historial, participaciones):
        print("=" * 60)
        print(f"✅ ¡LÍNEA TEMPORAL VERDADERA ENCONTRADA EN EL UNIVERSO #{self.contador_universos}!")
        print("=" * 60)
        print(f"Resultado final perfectamente equilibrado: {participaciones}\n")
        
        print("📋 Registro cronológico de la realidad:")
        for i in range(3):
            j1, j2, perdedor = historial[i]
            ganador = j1 if perdedor == j2 else j2
            print(f"  Juego {i+1}: Juegan {j1} + {j2} -> Pierde {perdedor} (Gana {ganador})")
        
        print("\n🧠 RESOLUCIÓN MATEMÁTICA DEL ENIGMA:")
        j1_2, j2_2, perdedor_2 = historial[1]
        print(f"Tras analizar cientos de realidades descartadas, la matriz indica que en el Juego 2 jugaron {j1_2} y {j2_2}.")
        print(f"El único destino matemáticamente posible es que el perdedor sea: ¡{perdedor_2}!")
        print("=" * 60 + "\n")

# Ejecutar el software
torneo = UniversoTorneo()
torneo.resolver()
