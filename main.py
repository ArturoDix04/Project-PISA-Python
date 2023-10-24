import time
try:
  def ciencias_modulo_1_bio():
      suma=0
      x=0
      #Problema 1
      while x<3:
          print('1.-¿Qué es el ADN? \n')
          print(' a) Una sustancia presente en las membranas celulares que \n impide que se salga el contenido de la célula.') 
          print(' b) Una molécula que contiene las instrucciones para la \n fabricación de nuestros cuerpos.')
          print(' c) Una proteína presente en la sangre que ayuda a transportar \n oxígeno a los tejidos.' )
          print(' d) Una hormona de la sangre que ayuda a regular el contenido \n de glucosa en las células del cuerpo. ' + '\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='b' and x<3:
              x=x+1
              if n.lower()!='b' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 2:
      while x<3:
          print('2.-Puede suceder, después de una operación, que los pacientes sean incapaces de \n comer y de beber, y entonces se les pone un gota a gota con suero que contiene \n agua, azúcares y sales minerales. A veces también se le añaden antibióticos y \n  tranquilizantes. \n ')
          print('¿Por qué los azúcares que se añaden al gota a gota son importantes \n para el paciente recién operado? \n')
          print('a) Para evitar la deshidratación. \n'+ 'b) Para controlar el dolor del postoperatorio. \n'+ 'c) Para curar las infecciones del postoperatorio. \n'+ 'd) Para proporcionar la nutrición necesaria. \n') 
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='d':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='d' and x<3: #Aquí si la respuesta es distinta a la correcta
              x=x+1 #se le suma uno a x para que vuelva a entrar al while pero con una oportunidad menos
              if n.lower()!='d' and x==3: #si 
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 3:
      while x<1:
          print('3.-¿Cuáles son los beneficios del ejercicio físico practicado con regularidad? \n')
          print('a) El ejercicio físico ayuda a prevenir las enfermedades del \n corazón y los problemas circulatorios. \n'+ 'b) El ejercicio físico hace que tengas una dieta saludable. \n' )
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=1
              suma=suma+10
          if n.lower()!='a':
              print('Respuesta incorrecta \n')
      x=0
      
      #Problema 4:
      while x<1:
          print('4.-¿Qué sucede cuando se ejercitan los músculos? \n')
          print('a)Los músculos reciben un mayor flujo de sangre. \n'+ 'b) Se forma grasa en los músculos \n')
          n=input('Ingresa el inciso correcto: ') 
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=1
              suma=suma+10
          if n.lower()!='a':
              print('Respuesta incorrecta \n')
      x=0
      
      #Problema 5:
      while x<3:
          print('5.-¿Cuál de las siguientes funciones es propia del pulmón? \n')
          print('a) Bombear sangre oxigenada a todas las partes del cuerpo. \n'+ 'b) Transferir el oxígeno del aire que respiras a la sangre \n'+ 'c) Purificar la sangre reduciendo a cero su contenido en \n dióxido de carbono. \n'+ 'd) Transformar las moléculas de dióxido de carbono en \n moléculas de oxígeno. \n')
          n=input('Ingresa el inciso correcto: ') 
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='b' and x<3:
              x=x+1
              if n.lower()!='b' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
        
      #Problema 6:
      while x<2:
          print('6.-Fumar tabaco aumenta el riesgo de padecer cáncer de pulmón y otras enfermedades')
          print('a) VIH / SIDA \n'+ 'b) Varicela \n'+ 'c) Enfermedad cardiaca \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=2
              suma=suma+10
          if n.lower()!='c' and x<2:
              x=x+1
              if n.lower()!='c' and x==2:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
       #Problema 7:
      while x<3:
          print('7.- ¿Cuál es el papel de las bacterias en la aparición de la caries dental? \n')
          print('a) Las bacterias producen esmalte.\n'+ 'b) Las bacterias producen azúcar. \n'+ 'c) Las bacterias producen minerales. \n'+ 'd) Las bacterias producen ácido. \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='d':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='d' and x<3:
              x=x+1
              if n.lower()!='d' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 8:
      while x<2:
          print('8.-¿Frente a qué tipo de enfermedades se puede vacunar a la gente? \n')
          print('a) Enfermedades hereditarias como la hemofilia. \n'+ 'b) Enfermedades causadas por virus, como la polio. \n'+ 'c) Enfermedades causadas por un mal funcionamiento del cuerpo, como la diabetes. \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=2
              suma=suma+10
          if n.lower()!='b' and x<2:
              x=x+1
              if n.lower()!='b' and x==2:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 9:
      while x<1:
          print('9.-Si los animales o las personas padecen una enfermedad infecciosa bacteriana \n y luego se recuperan, el tipo de bacteria causante de la enfermedad, \n en general, no vuelve a infectarlos.')
          print('a) El cuerpo ha matado todas las bacterias que pueden producir la misma  enfermedad. \n'+ 'b) El cuerpo ha fabricado anticuerpos que matan este tipo de bacterias antes de que se multipliquen. \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=1
              suma=suma+10
          if n.lower()!='b':
              print('Respuesta incorrecta \n')
      x=0
      
      #Problema 10:
      while x<3:
          print('10.- A menudo, el anestésico es administrado en forma de gas, \n utilizando una mascarilla facial que recubre la nariz y la boca. \n')
          print('¿Están implicados en la acción de estos gases anestésicos los siguientes \n sistemas del cuerpo humano? Selecciona los que  cumplan con este criterio \n')
          print('a) Sistema digestivo \n'+ 'b) Sistema circulatorio \n'+ 'c) Sistema nervioso \n'+ 'd) Sistema respiratorio \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      return(suma)
  def ciencias_modulo_2_geo():
      suma=0
      x=0
      #Problema 1
      while x<3:
          print('1.-La potabilización del agua suele hacerse en varias etapas, \n que requieren técnicas diferentes. El proceso \n de potabilización mostrado en la figura comprende cuatro etapas. \n En la segunda etapa, el agua se recoge en un decantador. ')
          print('¿De qué forma contribuye esta etapa a que el agua esté más limpia? \n')
          print('a) El agua se hace menos ácida. \n'+ 'b) Las bacterias del agua mueren. \n'+ 'c) Se añade oxígeno al agua. \n'+ 'd) La grava y la arena se depositan en el fondo. \n'+ 'e) Las sustancias tóxicas se descomponen. \n') 
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='d':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='d' and x<3:
              x=x+1
              if n.lower()!='d' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 2:
      while x<3:
          print('2.-¿Cuál de las afirmaciones siguientes es la más adecuada \n para la teoría científica de la evolución? \n ')
          print('a) No se puede creer la teoría porque es imposible ver \n cómo cambian las especies. \n'+ 'b) La teoría de la evolución es posible para los animales pero \n no se puede aplicar a los seres humanos. \n'+ 'c) La evolución es una teoría científica que actualmente \n se basa en numerosas observaciones \n'+ 'd) La teoría de la evolución se ha comprobado mediante \n experimentos científicos. \n') 
          n=input('Ingresa el inciso correcto: ')
          print('\n')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 3:
      while x<3:
          print('3.-¿Qué frase explica por qué hay día y noche en la Tierra? \n')
          print('a) La Tierra gira alrededor de su eje. \n'+ 'b) El Sol gira alrededor de su eje. \n'+'c) El eje de la Tierra está inclinado. \n'+ 'd) La Tierra gira alrededor del Sol. \n' )
          n=input('Ingresa el inciso correcto: ')
          print('\n')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 4:
      while x<3:
        print('4.-La temperatura en el Gran Cañón varía de menos de 0 °C \n a más de 40 °C. Aunque la  zona es desértica, las grietas \n de las rocas a veces contienen agua. ¿De qué manera estos \n cambios de temperatura y la presencia de agua en las grietas \n de las rocas contribuyen a acelerar el desmenuzamiento de las rocas? \n')
        print('a) El agua congelada disuelve las rocas calientes. \n'+ 'b) El agua cementa a las rocas entre sí. \n'+ 'c) El hielo pule la superficie de las rocas. \n'+ 'd) El agua congelada se dilata en las grietas de las rocas. \n')
        n=input('Ingresa el inciso correcto: ')
        if n.lower()=='d':
            print('¡Es correcto! \n')
            x=3
            suma=suma+10
        if n.lower()!='d' and x<3:
            x=x+1
            if n.lower()!='d' and x==3:
                print('Agotaste tus intentos \n')
            else:
                print('Respuesta incorrecta, trata nuevamente \n')
      x=0
        
      #Problema 5:
      while x<3:
          print('5.-De los planetas siguientes, ¿cuál puede ser observado \n algunas veces desde la Tierra en tránsito delante del Sol? \n')
          print('a) Mercurio \n'+ 'b) Marte \n'+'c) Júpiter \n'+ 'd) Saturno \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      
      return(suma)
  def ciencias_modulo_3_fisica():
      suma=0
      x=0
      #Problema 1
      while x<3:
          print('1.-Un autobús circula por un tramo recto de carretera. Raimundo, el conductor \n del autobús, tiene un vaso de agua sobre el panel de mandos: \n', 'De repente, Raimundo tiene que frenar violentamente. \n')
          print('¿Qué es más probable que le ocurra al agua del vaso inmediatamente \n  después de que Raimundo frene violentamente? \n')
          print('a) El agua permanecerá horizontal. \n'+ 'b) El agua se derramará por el lado 1. \n'+ 'c) El agua se derramará por el lado 2. \n'+ 'd) El agua se derramará, pero no sabes si lo hará \n por el lado 1 o por el lado 2. \n' ) 
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 2:
      while x<3:
          print('2.-Para beber durante el día, Pedro tiene una taza con café caliente, \n a unos 90 ºC de temperatura, y una taza con agua mineral fría, \n a unos 5 ºC de temperatura. Las tazas son del mismo material \n y tamaño, y el volumen contenido en cada taza es el mismo. \n Pedro deja las tazas en una habitación donde la temperatura \n es de unos 20 ºC.  \n ')
          print('¿Cuáles serán probablemente las temperaturas del café \n y del agua mineral después de 10 minutos? \n')
          print('a) 70 ºC y 10 ºC. \n'+ 'b) 90 ºC y 5 ºC. \n'+ 'c) 70 ºC y 25 ºC. \n'+ 'd) 20 ºC y 20 ºC. \n') 
          n=input('Ingresa el inciso correcto: ')
          print('\n')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      return(suma)
  def ciencias_modulo_4_quimica():
      suma=0
      x=0
      #Problema 1
      while x<3:
          print('1.-Un cocinero hace el pan mezclando harina, agua, sal y levadura. \n Una vez mezclado todo, coloca la mezcla en un recipiente durante varias \n horas para que se produzca el proceso de la fermentación.\n Durante la fermentación, se produce un cambio químico en la mezcla: \n la levadura (un hongo unicelular) transforma el almidón y los azúcares de la \nharina en dióxido de carbono y alcohol. \n')
          print('La fermentación hace que la mezcla se hinche. ¿Por qué se hincha? \n')
          print('a) Se hincha porque se produce alcohol, que se transforma en gas. \n'+ 'b) Se hincha porque los hongos unicelulares se reproducen dentro de ella. \n'+ 'c) Se hincha porque se produce un gas, el dióxido de carbono. \n'+ 'd) Se hincha porque la fermentación transforma el agua líquida en vapor. \n' ) 
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 2:
      while x<3:
          print('2.-Cuando la mezcla de pan hinchada (fermentada) se cuece en el horno, \n las burbujas de gas y vapor que hay en la mezcla \n se dilatan. \n ')
          print(' ¿Por qué se dilatan los gases y los vapores al calentarse? \n')
          print('a) Sus moléculas se hacen más grandes. \n'+ 'b) Sus moléculas se mueven más deprisa. \n'+ 'c) Aumenta su número de moléculas. \n'+ 'd) Sus moléculas entran en colisión con menos frecuencia. \n') 
          n=input('Ingresa el inciso correcto: ') 
          print('\n')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='b' and x<3:
              x=x+1
              if n.lower()!='b' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 3:
      while x<3:
          print('3.-En la mezcla, la levadura transforma el almidón y \n los azúcares de la harina mediante una reacción química en la \n que se producen dióxido de carbono y alcohol. \n')
          print('¿De dónde provienen los átomos de carbono que forman \n parte del dióxido de carbono y del alcohol? \n')
          print('a) Algunos átomos de carbono provienen de los azúcares. \n'+ 'b) Algunos átomos de carbono formaban parte \n de las moléculas de sal. \n'+ 'c) Algunos átomos de carbono provienen del agua. \n'+ 'd) Los átomos de carbono se formaron a partir de otros elementos \n en una reacción química. \n' )
          n=input('Ingresa el inciso correcto: ')
          print('\n')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 4:
      while x<3:
          print('4.-Una astilla de mármol tiene una masa de 2,0 gramos \n antes de ser sumergida en vinagre durante toda una noche. \n Al día siguiente, la astilla se extrae y se seca. \n ¿Cuál será la masa de la astilla de mármol seca? \n')
          print('a)Menos de 2,0 gramos. \n'+ 'b)  Exactamente 2,0 gramos. \n'+ 'c) Entre 2,0 y 2,4 gramos. \n'+ 'd) Más de 2,4 gramos. \n' )
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      
      x=0
      #Problema 5:
      while x<3:
          print('5.-Aceites y ceras son sustancias que se mezclan bien entre sí. \n El agua no se mezcla con los aceites, y las ceras no son \n solubles en agua. \n')
          print('Si se vuelca mucha agua dentro de la mezcla de la barra \n de labios cuando se está calentando, ¿qué ocurrirá \n con mayor probabilidad? \n')
          print('a) Se producirá una mezcla más cremosa y blanda. \n'+ 'b) La mezcla se hará más dura. \n'+ 'c) La mezcla apenas cambiará. \n'+ 'd) Grumos grasos de la mezcla flotarán sobre el agua. \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='d':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='d' and x<3:
              x=x+1
              if n.lower()!='d' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      return(suma)
  def ciencias_modulo_5_tecnologia():
      suma=0
      x=0
      #Problema 1
      while x<3:
          print('1.-¿Por qué se pueden observar más estrellas en el campo \n que en las ciudades donde vive la mayoría de la gente? \n')
          print('a) La luna es más luminosa en las ciudades y amortigua \n la luz de muchas estrellas. \n '+ 'b) Hay más polvo que refleja la luz en el aire \n del campo que en el aire de la ciudad. \n'+ 'c) La luminosidad de las luces de la ciudad dificulta la \n visibilidad de las estrellas. \n'+ 'd) El aire de la ciudad es más caliente por el calor \n que emiten los coches, las máquinas y las casas. \n' ) 
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 2:
      while x<3:
          print('2.-Para observar estrellas de escaso brillo, \n Tomás utiliza un telescopio con una lente de gran diámetro. \n ')
          print(' ¿Por qué un telescopio con una lente de gran diámetro \n permite observar las estrellas de escaso brillo? \n')
          print('a) Cuanto mayor es la lente más luz capta. \n'+ 'b) Cuanto mayor es la lente mayor es el aumento. \n'+ 'c) Las lentes grandes permiten ver más cantidad de cielo. \n'+ 'd) Las lentes grandes detectan los colores oscuros en \n las estrellas. \n') 
          n=input('Ingresa el inciso correcto: ') 
          print('\n')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 3:
      while x<3:
          print('3.-¿Qué instrumento del equipo del laboratorio sería el \n instrumento que necesitarías para comprobar que la tela \n es conductora de la electricidad? \n')
          print('a) Un voltímetro. \n'+ 'b) Un fotómetro. \n'+ 'c) Un micrómetro. \n'+ 'd) Un sonómetro. \n' )
          n=input('Ingresa el inciso correcto: ')
          print('\n')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      
      return(suma)
  def ciencias_examen_final():
      suma=0
      x=0
      #Problema 1
      while x<3:
          print('1.-La potabilización del agua suele hacerse en varias etapas, \n que requieren técnicas diferentes. El proceso \n de potabilización mostrado en la figura comprende cuatro etapas. \n En la segunda etapa, el agua se recoge en un decantador. ')
          print('¿De qué forma contribuye esta etapa a que el agua esté más limpia? \n')
          print('a) El agua se hace menos ácida. \n'+ 'b) Las bacterias del agua mueren. \n'+ 'c) Se añade oxígeno al agua. \n'+ 'd) La grava y la arena se depositan en el fondo. \n'+ 'e) Las sustancias tóxicas se descomponen. \n') 
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='d':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='d' and x<3:
              x=x+1
              if n.lower()!='d' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 2:
      while x<3:
          print('2.-Para beber durante el día, Pedro tiene una taza con café caliente, \n a unos 90 ºC de temperatura, y una taza con agua mineral fría, \n a unos 5 ºC de temperatura. Las tazas son del mismo material \n y tamaño, y el volumen contenido en cada taza es el mismo. \n Pedro deja las tazas en una habitación donde la temperatura \n es de unos 20 ºC.  \n ')
          print('¿Cuáles serán probablemente las temperaturas del café \n y del agua mineral después de 10 minutos? \n')
          print('a) 70 ºC y 10 ºC. \n'+ 'b) 90 ºC y 5 ºC. \n'+ 'c) 70 ºC y 25 ºC. \n'+ 'd) 20 ºC y 20 ºC. \n') 
          n=input('Ingresa el inciso correcto: ')
          print('\n')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 3:
      while x<3:
          print('3.-Aceites y ceras son sustancias que se mezclan bien entre sí. \n El agua no se mezcla con los aceites, y las ceras no son \n solubles en agua. \n')
          print('Si se vuelca mucha agua dentro de la mezcla de la barra \n de labios cuando se está calentando, ¿qué ocurrirá \n con mayor probabilidad? \n')
          print('a) Se producirá una mezcla más cremosa y blanda. \n'+ 'b) La mezcla se hará más dura. \n'+ 'c) La mezcla apenas cambiará. \n'+ 'd) Grumos grasos de la mezcla flotarán sobre el agua. \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='d':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='d' and x<3:
              x=x+1
              if n.lower()!='d' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 4:
      while x<3:
          print('4.-¿Qué es el ADN? \n')
          print(' a) Una sustancia presente en las membranas celulares que \n impide que se salga el contenido de la célula.') 
          print(' b) Una molécula que contiene las instrucciones para la \n fabricación de nuestros cuerpos.')
          print(' c) Una proteína presente en la sangre que ayuda a transportar \n oxígeno a los tejidos.' )
          print(' d) Una hormona de la sangre que ayuda a regular el contenido \n de glucosa en las células del cuerpo. ' + '\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='b' and x<3:
              x=x+1
              if n.lower()!='b' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 5:
      while x<3:
          print('5.-¿Qué frase explica por qué hay día y noche en la Tierra? \n')
          print('a) La Tierra gira alrededor de su eje. \n'+ 'b) El Sol gira alrededor de su eje. \n'+'c) El eje de la Tierra está inclinado. \n'+ 'd) La Tierra gira alrededor del Sol. \n' )
          n=input('Ingresa el inciso correcto: ')
          print('\n')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 6
      while x<3:
          print('6.-Un autobús circula por un tramo recto de carretera. Raimundo, el conductor \n del autobús, tiene un vaso de agua sobre el panel de mandos: \n', 'De repente, Raimundo tiene que frenar violentamente. \n')
          print('¿Qué es más probable que le ocurra al agua del vaso inmediatamente \n  después de que Raimundo frene violentamente? \n')
          print('a) El agua permanecerá horizontal. \n'+ 'b) El agua se derramará por el lado 1. \n'+ 'c) El agua se derramará por el lado 2. \n'+ 'd) El agua se derramará, pero no sabes si lo hará \n por el lado 1 o por el lado 2. \n' ) 
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 7:
      while x<3:
          print('7.-¿Cuál de las siguientes funciones es propia del pulmón? \n')
          print('a) Bombear sangre oxigenada a todas las partes del cuerpo. \n'+ 'b) Transferir el oxígeno del aire que respiras a la sangre \n'+ 'c) Purificar la sangre reduciendo a cero su contenido en \n dióxido de carbono. \n'+ 'd) Transformar las moléculas de dióxido de carbono en \n moléculas de oxígeno. \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='b' and x<3:
              x=x+1
              if n.lower()!='b' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 8:
      while x<3:
          print('8.-¿Qué instrumento del equipo del laboratorio sería el \n instrumento que necesitarías para comprobar que la tela \n es conductora de la electricidad? \n')
          print('a) Un voltímetro. \n'+ 'b) Un fotómetro. \n'+ 'c) Un micrómetro. \n'+ 'd) Un sonómetro. \n' )
          n=input('Ingresa el inciso correcto: ')
          print('\n')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      #Problema 9
      while x<3:
          print('9.- A menudo, el anestésico es administrado en forma de gas, \n utilizando una mascarilla facial que recubre la nariz y la boca. \n')
          print('¿Están implicados en la acción de estos gases anestésicos los siguientes \n sistemas del cuerpo humano? Selecciona los que  cumplan con este criterio \n')
          print('a) Sistema digestivo \n'+ 'b) Sistema circulatorio \n'+ 'c) Sistema nervioso \n'+ 'd) Sistema respiratorio \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='a':
            print('¡Es correcto! \n')
            x=3
            suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0 
      #Problema 10:
      while x<2:
          print('10.-Fumar tabaco aumenta el riesgo de padecer cáncer de pulmón y otras enfermedades')
          print('a) VIH / SIDA \n'+ 'b) Varicela \n'+ 'c) Enfermedad cardiaca \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=2
              suma=suma+10
          if n.lower()!='c' and x<2:
              x=x+1
              if n.lower()!='c' and x==2:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      return(suma)
  def matematicas_modulo_1_arit():
      suma=0
      x=0
      #Problema 1
      while x<3:
          print('1.- Desarrolla la siguiente multiplicación de binomios \n')
          print('(x+3)(x-12) \n')
          print(' a) x^2-9x-36 \n' ,'b) x^2-7x-27 \n' ,'c) x^2-8x-36 \n','d) x^2-12x-30 \n')
          n=input('Ingresa el inciso correcto: ' )
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
              
      x=0
      #Problema 2:
      while x<3:
          print('2.-En un concierto de rock se reservó para el público un terreno rectangular \n con unas dimensiones de 100 m por 50 m, se vendieron todas las entradas y \n el terreno se llenó de aficionados, todos de pie. \n')
          print('¿Cuál de las siguientes constituye la mejor estimación del número total \n de asistentes al concierto? \n')
          print(' a) 2.000 \n', 'b) 5.000 \n', 'c) 20.000 \n', 'd) 50.000 \n' , 'e) 100.000 \n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 3:
      while x<3:
          print('3.-Factoriza la siguiente diferencia de cuadrados \n')
          print('9x^4-64y^6 \n')
          print('\n')
          print(' a) (3x^2+8y^3)(x^2+8y^3) \n', 'b) (3x^2-8y^3)(3x^2+8y^3) \n', 'c) (3x^3-8y^2)(3x^1+8y^3) \n' , 'd) (3x^2-4y^3)(3x^2+16y^3) \n' )
          print('\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='b' and x<3:
              x=x+1
              if n.lower()!='b' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
              
      x=0
      
      #Problema 4:
      while x<3:
          print('4.-Mei-Ling, ciudadana de Singapur, estaba realizando los preparativos para ir a ')
          print('Sudáfrica como estudiante de intercambio durante 3 meses. Necesitaba cambiar')
          print('algunos dólares de Singapur (SGD) en rands sudafricanos (ZAR). \n')
          print('¿Cuál de las siguientes constituye la mejor estimación del número total')
          print(' Mei-Ling se enteró de que el tipo de cambio entre el dólar de Singapur y el rand')
          print('sudafricano era de: 1 SGD = 4,2 ZAR')
          print('Mei-Ling cambió 3.000 dólares de Singapur en rands sudafricanos con este  tipo de cambio')
          print('¿Cuánto dinero recibió Mei-Ling en rands sudafricanos?')
          print(' a) 12.000 \n', 'b) 12.600 \n', 'c) 20.000 \n', 'd) 10.000 \n', 'e) 100.000 \n')
          print('\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='b' and x<3:
              x=x+1
              if n.lower()!='b' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 5:
      while x<3:
          print('5.-La subida al Monte Fuji sólo está abierta al público desde el 1 de julio hasta el 27 de  ')
          print('agosto de cada año. Alrededor de unas 200.000 personas suben al Monte Fuji durante')
          print('este periodo de tiempo \n')
          print('Como media, ¿alrededor de cuántas personas suben al Monte Fuji cada día? \n')
          print('\n')
          print(' a) 340 \n', 'b) 710 \n', 'c) 3.400 \n', 'd) 7.100 \n', 'e) 7.400 \n')
          print('\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
        
      #Problema 6:
      while x<3:
          print('6.-Elena acaba de comprar una nueva bicicleta con un velocímetro situado en el manillar.')
          print('El velocímetro le indica a Elena la distancia que recorre y la velocidad media de trayecto \n')
          print('Elena recorrió 6 km hasta la casa de su tía. El velocímetro marcó una velocidad media')
          print('de 18 km/h para todo el trayecto. \n')
          print('¿Cuál de las siguientes afirmaciones es la correcta? \n')
          print('\n')
          print(' a) A Elena le llevó 20 minutos llegar a casa de su tía. \n', 'b) A Elena le llevó 30 minutos llegar a casa de su tía. \n', 'c) A Elena le llevó 3 horas llegar a casa de su tía \n' , 'd) No se puede decir cuánto tiempo le llevó a Elena llegar a casa de su tía. \n')
          print('\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='a':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='a' and x<3:
              x=x+1
              if n.lower()!='a' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
       #Problema 7:
      while x<3:
          print('7.- Desarrolla el siguiente binomio al cuadrado \n')
          print('(x-5)^2 \n')
          print('\n')
          print(' a) x^2+10x+25 \n', 'b) x^2-5x+10 \n', 'c) x^2-5x+25 \n', 'd) x^2-10x+25 \n')
          print('\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='d':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='d' and x<3:
              x=x+1
              if n.lower()!='d' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 8:
      while x<3:
          print('8.-Para construir una estantería un carpintero necesita lo siguiente:  ')
          print(' 4 tablas largas de madera \n', '6 tablas cortas de madera \n', '12 ganchos pequeños \n', '2 ganchos grandes \n', '14 tornillos \n')
          print('El carpintero tiene en el almacén 26 tablas largas de madera,')
          print('33 tablas cortas de madera, 200 ganchos pequeños')
          print('20 ganchos grandes y 510 tornillos. \n')
          print('¿Cuántas estanterías completas puede construir este carpintero? \n')
          print(' a) 7 estanterías \n', 'b) 5 estanterías \n', 'c) 4 estanterías \n', 'd) 3 estanterías \n')
          print('\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='b':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='b' and x<3:
              x=x+1
              if n.lower()!='b' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 9:
      while x<3:
          print('9.-Normalmente, una pareja de pingüinos pone dos huevos al año. Por lo general, ')
          print('el polluelo del mayor de los dos huevos es el único que sobrevive.')
          print('En el caso de los pingüinos de penacho amarillo, el primer huevo, pesa aproximadamente')
          print('78 g y el segundo huevo pesa aproximadamente 110 g. \n')
          print('Aproximadamente, ¿en qué porcentaje es más pesado el segundo huevo que el primer huevo? \n')
          print(' a) 29% \n', 'b) 32% \n', 'c) 41% \n', 'd) 71% \n')
          print('\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      x=0
      
      #Problema 10:
      while x<3:
          print('10.-Estás preparando tu propio aliño para la ensalada. ')
          print('He aquí una receta para 100 mililitros (ml) de aliño.')
          print(' Aceite para ensalada: 60 ml \n', 'Vinagre: 30 ml \n', 'Salsa de soja: 10 ml \n')
          print('¿Cuántos mililitros (ml) de aceite para ensalada necesitas para preparar ')
          print('para preparar 150 ml de este aliño? \n')
          print(' a) 80 ml \n', 'b) 86 ml \n', 'c) 90 ml \n', 'd) 77 ml \n')
          print('\n')
          n=input('Ingresa el inciso correcto: ')
          if n.lower()=='c':
              print('¡Es correcto! \n')
              x=3
              suma=suma+10
          if n.lower()!='c' and x<3:
              x=x+1
              if n.lower()!='c' and x==3:
                  print('Agotaste tus intentos \n')
              else:
                  print('Respuesta incorrecta, trata nuevamente \n')
      return(suma)
  def matematicas_modulo_2_funciones (): #dixfunciones
    suma=0
    x=0
    #Problema 1
    while x<2:
      print('1.- ¿A qué llamamos Dominio de una función? \n')
      print(' a) El dominio de una función está formado por aquellos valores de y para los que se puede calcular x \n' ,'b) El dominio de una función está formado por aquellos valores de x para los que se puede calcular la imagen f(x). \n' ,'c) El dominio de una función esta formado por los valores que no participan de la relación\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=2
        suma=suma+20
      if n.lower()!='b' and x<2:
        x=x+1
        if n.lower()!='b' and x==2:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
    #Problema 2
    while x<3:
      print("2.- ¿Cómo se llama un punto en la gráfica al que ésta llega en forma decreciente para, a partir de ese punto, continuar en forma creciente? \n")
      print(" a) Máximo \n b) Mínimo \n c) Vértice \n d) Ordenada al origen\n")
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+20
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
    
    #Problema 3
    while x<3:
      print("3.- ¿Qué función de las siguientes corresponde a una parábola? \n")
      print(" a) Ninguna \n b) y = 3x + 4 \n c) y = x^2 \n d) y = 1/x\n")
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='c':
        print('¡Es correcto! \n')
        x=3
        suma=suma+20
      if n.lower()!='c' and x<3:
        x=x+1
        if n.lower()!='c' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
    #Problema 4
    while x<3:
      print("4.- ¿Cuál es el vértice de la siguiente función?\n")
      print("y = -3x^2 + 12x - 27")
      print(" a) 1/4 \n b) 2\n c) -1/4 \n d) -2\n ")
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+20
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')            
    x=0
  
    #Problema 5
    while x<3:
      print("5.- ¿Cuántas veces puede una función cortar al eje de ordenada?\n")
      print(" a) Ninguna \n b) 1 \n c)2 \n d) infinitas veces\n ")
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+20
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')            
    x=0
    return (suma)
  def matematicas_modulo_3_estadistica ():
    suma=0
    x=0
    #Problema 1
    while x<3:
      print('1.- ¿Cuáles son los tipos de variables que existen? \n')
      print(' a) Algebraicas/Continuas \n' ,'b) Cuantitativas/Cualitativas \n' ,'c) Discontinuas/Nominales \n d) Cualitativas/Racionales\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+12.5
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 2
    while x<3:
      print('2.- ¿Qué es un censo? \n')
      print(' a) Un dato prevenible \n' ,'b) Un dato previsible \n' ,'c) Es un padrón polista asociado al censo racional, que permite delimitar un conteo estadística \n d) Es un padrón o lista asociado al censo poblacional, que permite delimitar una población estadística\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='d':
        print('¡Es correcto! \n')
        x=3
        suma=suma+12.5
      if n.lower()!='d' and x<3:
        x=x+1
        if n.lower()!='d' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 3
    while x<2:
      print('3.- Tipos de muestreo probabilístico \n')
      print(' a) Aleatorio simple, mediante tablas, sistemático, estratificado, conglomerado \n' ,'b) Aleatorio crítico, mediante gráficos, sistemas, conjugado \n' ,'c) Referencial, No probabilístico, simple, compuesto \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='a':
        print('¡Es correcto! \n')
        x=2
        suma=suma+12.5
      if n.lower()!='a' and x<2:
        x=x+1
        if n.lower()!='a' and x==2:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 4
    while x<2:
      print('4.- ¿Cómo se saca la moda en excel? \n')
      print(' a) =MODA(numero1;numero 2…) \n' ,'b) =MODA() \n' ,'c) =MODA(numeroA ;numero 2…) \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='a':
        print('¡Es correcto! \n')
        x=2
        suma=suma+12.5
      if n.lower()!='a' and x<2:
        x=x+1
        if n.lower()!='a' and x==2:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 5
    while x<3:
      print('5.- ¿Qué es el espacio muestral?\n')
      print(' a) Conjunto de muestras que se pueden obtener \n b) Selección de muestra \n c) Conjunto de muestras que no se pueden obtener \n d) Cantidad de muestra \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='a':
        print('¡Es correcto! \n')
        x=3
        suma=suma+12.5
      if n.lower()!='a' and x<3:
        x=x+1
        if n.lower()!='a' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 6
    while x<3:
      print('6.- ¿Qué es el parámetro?\n')
      print(' a) Herramienta de investigación científica, cuya función básica es determinar que parte de la población debe examinarse. \n' ,'b) Permite delimitar una población estadística que refleja el número total de individuos de un territorio \n c) Es un valor que indica el grado de variación disjunta de dos variables aleatorias respecto sus medidas \n d) Valor, medida o indicador representativo de la población que se selecciona para ser estudiado \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='d':
        print('¡Es correcto! \n')
        x=3
        suma=suma+12.5
      if n.lower()!='d' and x<3:
        x=x+1
        if n.lower()!='d' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 7
    while x<3:
      print('7.- ¿Qué es covarianza?\n')
      print(' a) Es un valor que no indica el grado de variación conjunta de dos variables aleatorias respecto sus medidas \n' ,'b) Es un valor que indica el grado de variación conjunta de dos variables aleatorias respecto sus medidas \n'' c) Es un valor que indica el grado de variación disjunta de dos variables aleatorias respecto sus medidas \n d) Valor, medida o indicador representativo de la población que se selecciona para ser estudiado \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+12.5
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 8
    while x<2:
      print('8.- En el diagrama de Pareto el ______de las quejas de los clientes son producto del ______ de nuestros defectos\n')
      print(' a) 70% de 30%  \n' ,'b) 30% de 70% \n c) 80% de 20% \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='c':
        print('¡Es correcto! \n')
        x=2
        suma=suma+12.5
      if n.lower()!='c' and x<2:
        x=x+1
        if n.lower()!='c' and x==2:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
    return (suma)
  def matematicas_modulo_4_probabilidad ():
    suma=0
    x=0
    #Problema 1
    while x<3:
      print('1.- Se tiene una urna con 8 bolas rojas, 5 amarillas y 7 verdes se extrae al azar ¿Cuál es la probabilidad de que salga verde? \n')
      print(' a) 0.35 \n' ,'b) 0.6 \n' ,'c) 0.4 \n d) 0.25\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10 
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 2
    while x<3:
      print('2.- Una bolsa contiene 2 bolas negras, 3 bolas blancas, 4 bolas rojas y 5 bolas verdes. Se extrae una bola de la bolsa, cuál es la probabilidad de obtener la bola verde? \n')
      print(' a) 3/14 \n' ,'b) 5/14 \n' ,'c) 4/14 \n d) 2/14\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 3
    while x<3:
      print('3.- Se lanza una moneda y un dado. Hallar la probabilidad que salga sello y numero impar. \n')
      print(' a) 1/5 \n' ,'b) 1/6 \n' ,'c) 1/4 \n d) 1/12\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='c':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='c' and x<3:
        x=x+1
        if n.lower()!='c' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 4
    while x<3:
      print('4.- Halle el espacio muestral del lanzamiento de 3 monedas\n')
      print(' a) CCC,CCS,CSC,CSS,SCS \n' ,'b) CCC, CCS, CSC, CSS, SCC, SCS, SSC, SSS \n' ,'c) SCS,CSS,CCC,SCS \n d) SCS,CCC,SCC,CCS,CSS,CSC\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 5
    while x<3:
      print('5.- ¿Cuál es la probabilidad de que al lanzar 3 monedas se obtengan al menos 2 caras?\n')
      print(' a) 4/8 (100) = 50% \n' ,'b)2/2 (100) = 100% \n' ,'c) 3/8 (100) = 37.5% \n d) 1/3 (100) = 33.3%\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='a':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='a' and x<3:
        x=x+1
        if n.lower()!='a' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 6
    while x<3:
      print('6.- Luego de lanzar 2 dados. Calcula la probabilidad de que la suma sea 5 o 3\n')
      print(' a) 6/30 (100) = 20% \n' ,'b) 5/36 (100) = 13.8% \n' ,'c) 4/30 (100) = 13.3% \n d) 6/36 (100) = 17%\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='d':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='d' and x<3:
        x=x+1
        if n.lower()!='d' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 7
    while x<3:
      print('7.- ¿De cuantas maneras distintas puede un obrero vestirse si posee: una camisa roja, una camisa azul, una camisa blanca; un pantalón azul, un pantalón negro, un pantalón café; un par de tenis y un par de zapatos?\n')
      print(' a) 16 \n' ,'b) 6 \n' ,'c) 12 \n d) 18 \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='d':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='d' and x<3:
        x=x+1
        if n.lower()!='d' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 8
    while x<3:
      print('8.- En una urna se tienen 12 fichas de diferentes figuras y colores: 4 círculos rojos, 3 triángulos amarillos, 2 cuadrados rojos y 3 rombos azules. Si se extrae cualquier ficha al azar, ¿Cuál es la probabilidad de obtener una de color rojo?\n')
      print(' a) 0.16 \n' ,'b) 0.25 \n' ,'c) 0.33 \n d) 0.5 \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='d':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='d' and x<3:
        x=x+1
        if n.lower()!='d' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 9
    while x<3:
      print('9.- Para evaluar diariamente el desempeño de los alumnos, un profesor hace dos preguntas al azar a diferentes personas, sobre lo visto en la clase anterior. Si en el salón hay 15 mujeres y 10 hombres, ¿Cuál es la probabilidad de que el profesor le haga la primera pregunta a un hombre? \n')
      print(' a) 1/10 \n' ,'b) 10/25 \n' ,'c) 1/2 \n d) 15/25 \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
    return (suma)
  def matematicas_modulo_5_final ():
    suma=0
    x=0
    #Problema 1
    while x<3:
      print('1.- Desarrolla la siguiente multiplicación de binomios \n')
      print('(x+3)(x-12) \n')
      print(' a) x^2-9x-36 \n' ,'b) x^2-7x-27 \n' ,'c) x^2-8x-36 \n','d) x^2-12x-30 \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='a':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='a' and x<3:
        x=x+1
        if n.lower()!='a' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')         
    x=0
  
    #Problema 2:
    while x<3:
      print('2.-Factoriza la siguiente diferencia de cuadrados \n')
      print('9x^4-64y^6 \n')
      print('\n')
      print(' a) (3x^2+8y^3)(x^2+8y^3) \n', 'b) (3x^2-8y^3)(3x^2+8y^3) \n', 'c) (3x^3-8y^2)(3x^1+8y^3) \n' , 'd) (3x^2-4y^3)(3x^2+16y^3) \n' )
      n=input('Ingresa el inciso correcto: ')
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')          
    x=0
  
    #Problema 3
    while x<3:
      print("3.- ¿Qué función de las siguientes corresponde a una parábola? \n")
      print(" a) Ninguna \n b) y = 3x + 4 \n c) y = x^2 \n d) y = 1/x\n")
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='c':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='c' and x<3:
        x=x+1
        if n.lower()!='c' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 4
    while x<3:
      print("4.- ¿Cuál es el vértice de la siguiente función?\n")
      print("y = -3x^2 + 12x - 27")
      print(" a) 1/4 \n b) 2\n c) -1/4 \n d) -2\n ")
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')            
    x=0
  
    #Problema 5
    while x<3:
      print('5.- ¿Qué es el espacio muestral?\n')
      print(' a) Conjunto de muestras que se pueden obtener \n b) Selección de muestra \n c) Conjunto de muestras que no se pueden obtener \n d) Cantidad de muestra \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='a':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='a' and x<3:
        x=x+1
        if n.lower()!='a' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 6
    while x<3:
      print('6.- ¿Qué es un censo? \n')
      print(' a) Un dato prevenible \n' ,'b) Un dato previsible \n' ,'c) Es un padrón polista asociado al censo racional, que permite delimitar un conteo estadística \n d) Es un padrón o lista asociado al censo poblacional, que permite delimitar una población estadística\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='d':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='d' and x<3:
        x=x+1
        if n.lower()!='d' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 7
    while x<3:
      print('7.- ¿De cuantas maneras distintas puede un obrero vestirse si posee: una camisa roja, una camisa azul, una camisa blanca; un pantalón azul, un pantalón negro, un pantalón café; un par de tenis y un par de zapatos?\n')
      print(' a) 16 \n' ,'b) 6 \n' ,'c) 12 \n d) 18 \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='d':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='d' and x<3:
        x=x+1
        if n.lower()!='d' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 8
    while x<3:
      print('8.- Para evaluar diariamente el desempeño de los alumnos, un profesor hace dos preguntas al azar a diferentes personas, sobre lo visto en la clase anterior. Si en el salón hay 15 mujeres y 10 hombres, ¿Cuál es la probabilidad de que el profesor le haga la primera pregunta a un hombre? \n')
      print(' a) 1/10 \n' ,'b) 10/25 \n' ,'c) 1/2 \n d) 15/25 \n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='b':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='b' and x<3:
        x=x+1
        if n.lower()!='b' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
  
    #Problema 9:
    while x<3:
      print('9.- Desarrolla el siguiente binomio al cuadrado \n')
      print('(x-5)^2 \n')
      print('\n')
      print(' a) x^2+10x+25 \n', 'b) x^2-5x+10 \n', 'c) x^2-5x+25 \n', 'd) x^2-10x+25 \n')
      print('\n')
      n=input('Ingresa el inciso correcto: ')
      if n.lower()=='d':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='d' and x<3:
        x=x+1
        if n.lower()!='d' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x=0
    
    #Problema 10
    while x<3:
      print('10.- ¿Cuál es la probabilidad de que al lanzar 3 monedas se obtengan al menos 2 caras?\n')
      print(' a) 4/8 (100) = 50% \n' ,'b)2/2 (100) = 100% \n' ,'c) 3/8 (100) = 37.5% \n d) 1/3 (100) = 33.3%\n')
      n=input('Ingresa el inciso correcto: ' )
      if n.lower()=='a':
        print('¡Es correcto! \n')
        x=3
        suma=suma+10
      if n.lower()!='a' and x<3:
        x=x+1
        if n.lower()!='a' and x==3:
          print('Agotaste tus intentos \n')
        else:
          print('Respuesta incorrecta, trata nuevamente \n')
    x = 0
    return (suma)
  def leer_mod_mat():
      archivo=open("menu_mat.txt","r")#Abre el archivo donde se encuentran los modulos y recursos de matemáticas
      lista=[]
      for line in archivo:
          linea_archivo=line.split("~")#Separa modulos de los recursos
          lista.append(linea_archivo) #Agrega los valores a la lista
      archivo.close() #Se cierra el archivo
      return lista#Regresa el valor de la lista
  
  def leer_mod_ciencias():
      archivo=open("menu_ciencias.txt","r")#Abre el archivo donde se encuentran los modulos y recursos de ciencias
      lista=[]
      for line in archivo:
          linea_archivo=line.split("~")#Separa modulos de los recursos
          lista.append(linea_archivo)#Agrega los valores a la lista
      archivo.close()#Se cierra el archivo
      return lista#Regresa el valor de la lista
  
  def main_c_b(nombre): 
      contes=input('Bienvenido al examen del Modulo 1: Ciencias,\n'+'si deseas comenzar ingresa la tecla s \n')
      if contes=='s':
          suma_cal= ciencias_modulo_1_bio()
          promedio= suma_cal/10
          print('Tu calificación final de este modulo es: ', promedio) 
          while promedio<7: #aquí regresa al examen para acreditarlo
              print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
              suma_cal= ciencias_modulo_1_bio()
              promedio= suma_cal/10
              print('Tu calificación final de este modulo es: ', promedio)
          if promedio>=7:
              a=str(nombre)+'~Modulo 1: Biología:~'+ str(promedio)+"\n"
              archivo=open("calificaciones.txt","a")
              archivo.write(a)
              archivo.close()
              print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')     #Main del examen ciencias biología Mod 1
  def main_c_g(nombre):
      contes=input('Bienvenido al examen de Ciencias Modulo 2: Geología,\n'+'si deseas comenzar ingresa la tecla s \n')
      if contes=='s':
          suma_cal= ciencias_modulo_2_geo()
          promedio= suma_cal/5
          print('Tu calificación final de este modulo es ', promedio)
          while promedio<7: #aquí regresa al examen para acreditarlo
              print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
              suma_cal= ciencias_modulo_2_geo()
              promedio= suma_cal/5
              print('Tu calificación final de este modulo es ', promedio)
          if promedio>=7:
              b=str(nombre)+'~Modulo 2: Geología:~'+ str(promedio)+"\n"
              archivo=open("calificaciones.txt","a")
              archivo.write(b)
              archivo.close()
              print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
              #aquí pasa al submenú de ciencias para presentar el siguiente modulo  #Main del examen ciencias geología Mod 2
  def main_c_f(nombre): 
      contes=input('Bienvenido al examen del Modulo 3: Física,\n'+'si deseas comenzar ingresa la tecla s \n')
      if contes=='s':
          suma_cal= ciencias_modulo_3_fisica()
          promedio= suma_cal/2
          print('Tu calificación final de este modulo es ', promedio) 
          while promedio<7: #aquí regresa al examen para acreditarlo
              print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
              suma_cal= ciencias_modulo_3_fisica()
              promedio= suma_cal/2
              print('Tu calificación final de este modulo es ', promedio)
          if promedio>=7:
              c=str(nombre)+'~Modulo 3: Física:~'+ str(promedio)+"\n"
              archivo=open("calificaciones.txt","a")
              archivo.write(c)
              archivo.close()
              print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
              #aquí pasa al submenú de ciencias para presentar el siguiente modulo     #Main del examen ciencias física Mod 3
  def main_c_q(nombre):
      contes=input('Bienvenido al examen de Ciencias Modulo 4: Química,\n'+'si deseas comenzar ingresa la tecla s \n')
      if contes=='s':
          suma_cal= ciencias_modulo_4_quimica()
          promedio= suma_cal/5
          print('Tu calificación final de este modulo es ', promedio) 
          while promedio<7: #aquí regresa al examen para acreditarlo
              print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
              suma_cal= ciencias_modulo_4_quimica()
              promedio= suma_cal/5
              print('Tu calificación final de este modulo es ', promedio)
          if promedio>=7:
              d=str(nombre)+'~Modulo 4: Química:~'+ str(promedio)+"\n"
              archivo=open("calificaciones.txt","a")
              archivo.write(d)
              archivo.close()
              print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
              #aquí pasa al submenú de ciencias para presentar el siguiente modulo   #Main del examen ciencias química Mod 4
  def main_c_t(nombre):
      contes=input('Bienvenido al examen de Ciencias Modulo 5: Tecnología,\n'+'si deseas comenzar ingresa la tecla s \n')
      if contes=='s':
          suma_cal= ciencias_modulo_5_tecnologia()
          promedio= suma_cal/3
          print('Tu calificación final de este modulo es ', promedio) 
          while promedio<7: #aquí regresa al examen para acreditarlo
              print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
              suma_cal= ciencias_modulo_5_tecnologia()
              promedio= suma_cal/3
              print('Tu calificación final de este modulo es ', promedio)
          if promedio>=7:
              e=str(nombre)+'~Modulo 5 Tecnología:~'+ str(promedio)+"\n"
              archivo=open("calificaciones.txt","a")
              archivo.write(e)
              archivo.close()
              print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
              #aquí pasa al submenú de ciencias para presentar el siguiente modulo    #Main del examen ciencias tecnologia Mod 5
  def main_ciencias_examen_final(nombre):
      contes=input('Bienvenido al examen final de ciencias,\n'+'si deseas comenzar, ingresa la tecla s \n')
      if contes=='s':
          suma_cal= ciencias_examen_final()
          promedio= suma_cal/10
          print('Tu calificación final de este modulo es ', promedio) 
          while promedio<7: #aquí regresa al examen para acreditarlo
              print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
              suma_cal= ciencias_examen_final()
              promedio= suma_cal/10
              print('Tu calificación final de este modulo es ', promedio)
          if promedio>=7:
              f=str(nombre)+'~Modulo 6:Examen Final Ciencias'+ "~"+str(promedio)+"\n"
              archivo=open("calificaciones.txt","a")
              archivo.write(f)
              archivo.close()
              print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
              #aquí pasa al submenú de mate para presentar el siguiente modulo  #Main del examen final ciencias
  def main_mat_mod_1(nombre):
    contes=input('Bienvenido al examen del Modulo 1: Aritmética,\n'+'si deseas comenzar, ingresa la tecla s \n')
    if contes=='s':
        suma_cal= matematicas_modulo_1_arit()
        promedio= suma_cal/10
        print('Tu calificación final de este modulo es ', promedio) 
        while promedio<7: #aquí regresa al examen para acreditarlo
          print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
          suma_cal= matematicas_modulo_1_arit()
          promedio= suma_cal/10
          print('Tu calificación final de este modulo es ', promedio)
        if promedio>=7:
          g=str(nombre)+'~Modulo 1: Aritmética'+ "~"+str(promedio)+"\n"
          archivo=open("calificaciones.txt","a")
          archivo.write(g)
          archivo.close()            
          print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo') #aquí pasa al submenú de mate para presentar el siguiente modulo
  def main_mat_mod_2(nombre):
    contes=input('Bienvenido al examen del Modulo 2: Funciones,\n'+'si deseas comenzar, ingresa la tecla s \n')
    if contes=='s':
      suma_cal= matematicas_modulo_2_funciones()
      promedio= suma_cal/10
      print('Tu calificación final de este modulo es ', promedio) 
      while promedio<7: #aquí regresa al examen para acreditarlo
        print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
        suma_cal= matematicas_modulo_2_funciones()
        promedio= suma_cal/10
        print('Tu calificación final de este modulo es ', promedio)
      if promedio>=7:
        g=str(nombre)+'~Modulo 2: Funciones'+ "~"+str(promedio)+"\n"
        archivo=open("calificaciones.txt","a")
        archivo.write(g)
        archivo.close()
        print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
  
  def main_mat_mod_3(nombre):
    contes=input('Bienvenido al examen del Modulo 3: Estadística,\n'+'si deseas comenzar, ingresa la tecla s \n')
    if contes=='s':
      suma_cal= matematicas_modulo_3_estadistica()
      promedio= suma_cal/10
      print('Tu calificación final de este modulo es ', promedio) 
      while promedio<7: #aquí regresa al examen para acreditarlo
        print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
        suma_cal= matematicas_modulo_3_estadistica()
        promedio= suma_cal/10
        print('Tu calificación final de este modulo es ', promedio)
      if promedio>=7:
        g=str(nombre)+'~Modulo 3: Estadística'+ "~"+str(promedio)+"\n"
        archivo=open("calificaciones.txt","a")
        archivo.write(g)
        archivo.close()
        print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
  def main_mat_mod_4(nombre):
    contes=input('Bienvenido al examen del Modulo 4: Probabilidad,\n'+'si deseas comenzar, ingresa la tecla s \n')
    if contes=='s':
      suma_cal= matematicas_modulo_4_probabilidad()
      promedio= suma_cal/9
      print('Tu calificación final de este modulo es ', promedio) 
      while promedio<7: #aquí regresa al examen para acreditarlo
        print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
        suma_cal= matematicas_modulo_4_probabilidad()
        promedio= suma_cal/9
        print('Tu calificación final de este modulo es ', promedio)
      if promedio>=7:
        g=str(nombre)+'~Modulo 4: Probabilidad'+ "~"+str(promedio)+"\n"
        archivo=open("calificaciones.txt","a")
        archivo.write(g)
        archivo.close()
        print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
  def main_mat_mod_5(nombre):
    contes=input('Bienvenido al examen del Modulo 5: Examen Final de Contenidos,\n'+'si deseas comenzar, ingresa la tecla s \n')
    if contes=='s':
      suma_cal= matematicas_modulo_5_final()
      promedio= suma_cal/10
      print('Tu calificación final de este modulo es ', promedio) 
      while promedio<7: #aquí regresa al examen para acreditarlo
        print('Modulo NO acreditado, por favor intenta nuevamente para avanzar al siguiente modulo')
        suma_cal= matematicas_modulo_5_final()
        promedio= suma_cal/10
        print('Tu calificación final de este modulo es ', promedio)
      if promedio>=7:
        g=str(nombre)+'~Modulo 5:Examen Final Matemáticas'+ "~"+str(promedio)+"\n"
        archivo=open("calificaciones.txt","a")
        archivo.write(g)
        archivo.close()
        print('Excelente, has acreditado esta sección, puedes pasar al siguiente modulo')
  def matematicas(nombre):
      print("\n    Ingresando a Matematicas...\n")
      time.sleep(1)#Se imprime un mensaje de espera
      print("Estos son los modulos a estudiar de matemáticas: ")
      modmat=leer_mod_mat()#modmat va a tener el valor de una lista de listas con la información de modulos y recursos
      for i in range(len(modmat)):
          for j in range(len(modmat[i])):
              print(modmat[i][j])#Imprime todos los valores dentro de la variable modmat, generando el menú de modulos y sus recursos
      modulos=["1","2","3","4","5"]#Opciones de input
      respuesta= input("\nPresione el numero de modulo de matemáticas a presentar (O escriba salir para regresar): ")
      respuesta=respuesta.lower()#se cambia a minusculas en caso que el usuario escriba SALIR o Salir
      while respuesta!="salir":
        while respuesta not in modulos:
          respuesta=input("No se pudo encontrar ese modulo, intentelo de nuevo: ")#Mensaje de error si se ingresa un modulo no existente
          respuesta.lower()
          if respuesta=="salir":
            print("")
            menu(nombre)
        if respuesta=="1":
          main_mat_mod_1(nombre)#Se ejecuta el examen del modulo 1
        if respuesta=="2":
          main_mat_mod_2(nombre)#Se ejecuta el examen del modulo 2
        if respuesta=="3":
          main_mat_mod_3(nombre)#Se ejecuta el examen del modulo 3
        if respuesta=="4":
          main_mat_mod_4(nombre)#Se ejecuta el examen del modulo 4
        if respuesta=="5":
          main_mat_mod_5(nombre)
          
        respuesta=input("\nPresione el numero de modulo a presentar (O escriba salir para regresar): ")
        respuesta=respuesta.lower()
        
    #http://educalab.es/inee/evaluaciones-internacionales/preguntas-liberadas-pisa-piaac/preguntas-pisa-matematicas
  def ciencias(nombre):
      print("\n    Ingresando a ciencias...\n")
      time.sleep(1)#Se imprime un mensaje de espera
      print("Estos son los modulos a estudiar de ciencias:")
      modcien=leer_mod_ciencias()#modcien va a tener el valor de una lista de listas con la información de modulos y recursos
      for i in range(len(modcien)):
          for j in range(len(modcien[i])):
              print(modcien[i][j])#Imprime todos los valores dentro de la variable modcien, generando el menú de modulos y sus recursos
      modulos=["1","2","3","4","5","6"]#Opciones de input
      respuesta= input("\nPresione el numero de modulo de ciencias a presentar (O escriba salir para regresar): ")
      respuesta=respuesta.lower()#se cambia a minusculas en caso que el usuario escriba SALIR o Salir
      while respuesta!="salir":
          while respuesta not in modulos:
              respuesta=input("\nNo se pudo encontrar ese modulo, intentelo de nuevo ")#Mensaje de error si se ingresa un modulo no existente
              respuesta.lower()
              if respuesta=="salir":
                print("")
                menu(nombre)
          if respuesta=="1":
              main_c_b(nombre)#Se ejecuta el examen del modulo 1
          if respuesta=="2":
              main_c_g(nombre)#Se ejecuta el examen del modulo 2
          if respuesta=="3":
              main_c_f(nombre)#Se ejecuta el examen del modulo 3
          if respuesta=="4":
              main_c_q(nombre)#Se ejecuta el examen del modulo 4
          if respuesta=="5":
              main_c_t(nombre)#Se ejecuta el examen del modulo 5
          if respuesta=="6":
              main_ciencias_examen_final(nombre)
          respuesta=input("\nPresione el numero de modulo a presentar (O escriba salir para regresar): ")
          respuesta=respuesta.lower()
  
  def menu (nombre):
      print("Este programa te brindará recursos que te serán útiles para la prueba PISA que evalúa conocimientos de matemáticas y ciencias. Este programa te ayudará con base en las necesidades que presentes de aprendizaje. \n")
      time.sleep (1)
      materia = input("Ingresa el número de acuerdo a la materia en la que requieres apoyo, 3 para ver calificaciones, o 4 para salir: \n1) Matemáticas \n2) Ciencias\n3) Calificaciones \n4) Salir\nIngrese el número: ")
      val=["1","2","3","4"]#Opciones de input
      while materia not in val : 
        materia=input("\nEl valor ingresado no es valido, vuelva a intentarlo \nIngrese nuevamente el valor: ")#Mensaje de error si se ingresa una materia no existente
      if materia == "1":
        matematicas (nombre)
        print("\n Regresando al menu principal...\n")
        time.sleep(1)
        menu(nombre)
      elif materia == "2": 
        ciencias (nombre)
        print("\n Regresando al menu principal...\n")
        time.sleep(1)
        menu(nombre)
      elif materia=="3":
        print()
        lista=[]
        archivo=open("calificaciones.txt","r")
        for line in archivo:
          linea_archivo=line.split("~")
          lista.append(linea_archivo)
        archivo.close()
        for i in lista:
          if i[0]==nombre:
            linea="{}{:>35}{:>12}".format(i[0],i[1],i[2])
            print(linea)
        menu(nombre)
        
      elif materia=="4":
        salir=input("Antes de salir, ¿desea guardar su progreso? s/n")
        opc=["s", "n"]
        while salir not in opc:
          salir=input("No se identificó su respuesta, ¿desea guardar su progreso? s/n")
        if salir!="s":
          archivo=open("calificaciones.txt","r+")
          archivo.truncate()
          archivo.close()
  
  
  nombre=str(input("Ingresa tu nombre: "))
  menu(nombre)
except ValueError:
  print("El valor ingresado no es válido. Asegúrese de escribir correctamente lo que se le pide. Se te regresará directamente al menú principal...")
  time.sleep (3)
  menu(nombre)
  
  