# Juego para rerpasar el primer nievel de lo aprendido
import random

titulo = "BIENVENIDO AL JUEGO DE TOMAR DECISIONES"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

print("En este juego pondrems a prueba tu habilidad de toma de decisiones. Tendrás que escoger bien para no morir.\n")
opcion = input("¿Deseas continuar?\n"
               "S - Si\n"
               "N - No\n"
               "Opción: ")
opcion = opcion.lower()

if opcion == "s":
    print("\nEstás en la calle escuachando música para pasar el rato. Te sientes solo y triste porque las cosas no han salido muy bien con tu chica.\n"
          "Han estado peleando últimamente porque te sientes celoso de uno de sus amigos ya que ella le está dando demasiada importancia a la relación\n"
          "que tiene con él. No quieres arruinarlo, pero en tu afán de querer hacer las cosas bien, lo arruinas… ")
    opcion = input("¿Quieres sentarte en una banca o prefieres seguir caminando?\n"
                   "A - Sentarte en una banca del parque\n"
                   "B - Seguir caminando\n"
                   "Opción: ")
    opcion = opcion.lower()

    if opcion == "a":
        print("\nTe sientas en una banca de un parque. Ves como la gente pasa tranquilamente por la calle mientras tú solamente te concentras en la música\n"
              "que proviene de tus audifonos. Cambias la canción.")
        opcion = input("Te ofrecen droga, ¿quieres?\n"
                       "S - Si\n"
                       "N - No\n"
                       "Opción: ")

        if opcion == "s":
            print("\nTe vuelves adicto a las drogras y ella te abandona, nadie quiere estar con alguien como tú.\n"
                  "Nadie te quiere  y muerers por sobredosis")

        elif opcion == "n":
            print("\nNo lo aceptas. Decides ir a casa, pero te encuentras con ella y su supuestio amigo en la subida a casa. Ves que se besan.\n"
                  "No dices nada, solo terminas destrozado. Lo siento, vivirás para sentirte mal por siempre.")

        else:
            print("\nNo eliges bien, así que te asaltan y te roban todo lo que traías contigo")

    elif opcion == "b":
        print("\nSigues caminado por las calles de la ciudad. Las luces de las farolas te iluminan. \n"
              "Te encuentras con tu chica, va caminando con el sujeto que más odias. Te sientes nervioso.")
        opcion = input("¿Los sigues?\n"
                       "S - Si\n"
                       "N - No\n"
                       "Opción: ")
        opcion = opcion.lower()

        if opcion == "n":
            print("\nDecide sentarte en una banca del parque. Pasan el tiempo y comienzas a sentirte tan mal que te desbordas y comienzas a llorar")
            opcion = input("¿Quieres irte a casa? \n"
                           "S - Si\n"
                           "N - No\n"
                           "Opción: ")
            opcion = opcion.lower()

            if opcion == "s":
                print("\nTe vas corrienda a casa. Esperas un momento antes de subir y te quedas miran el vacío de un puente mientras ves a tu chica que está \n"
                      "con el sujeto justo en frente de ti")
                opcion = input("¿Vas hacia ellos? \n"
                               "S - Si\n"
                               "N - No\n"
                               "Opción: ")
                opcion = opcion.lower()

            elif opcion == "n":
                print("\nEsperas un poco en esa banca. Decides ir a un bar a beber un poco para terminar con todo.\n"
                      "Te diriges a un bar lejado de donde estas y te encientras a un cholo que te reta a pelear")
                opcion = input("¿Peleas o huyes?\n"
                               "A - Pelear\n"
                               "B - Huyes\n"
                               "Opción: ")
                opcion = opcion.lower()

                if opcion == "a":
                    print("\nPeleas con el cholo, te golpea y quedas herido, pero al final ganas de alguna manera.\n"
                          "Consigues una navaja que le arrebataste al cholo\n"
                          "Vuelves a casa.")
                    navaja = True

                    print("\nTe vas a casa después de tu encuentro con ese pendejo. Te sientes mal porque te duelen los golpes que recibiste.\n"
                          "Al llegar a la subida a casa, ves a tu chica que se está despidiendo de su amigo abrazandolo.")
                    opcion = input("¿Vas hacia él?\n"
                                   "S - Si\n"
                                   "N - No\n"
                                   "Opción: ")
                    opcion = opcion.lower()

                    if opcion == "s":
                        print("\nCorres hacia él, lo tacleas y lo empiezas a perseguirlo.\n"
                              "La ves a ella preocupada por lo que está sucediendo, te pide que te detengas.")
                        opcion = input("¿Te detienes? \n"
                                       "S - Si\n"
                                       "N - No\n"
                                       "Opción: ")
                        opcion = opcion.lower()

                        if opcion == "s":
                            num1 = 5
                            num2 = random.randint(1, 20)
                            num3 = num1 * num2
                            print(f"\nElla te hace una pregunta rápida para que te tranquilices: \n")
                            opcion = int(input(f"¿Cuánto es el resultado de {num1} * {num2}?\n"
                                           f"Resultado = "))

                            if opcion == num3:
                                print("\nTe calmas, pero ella se va con él y te ves obligado a irte a casa.\n"
                                      "Puede que a la mañana siguiente ella regrese, pero tu al subir a la casa decides costarte las venas con la navaja del cholo.\n"
                                      "Te encuntran muerto")

                            elif opcion != num3:
                                print("\nNo acertaste la operación. Ella se enoja, te empuja y un automovil te atropella.\n"
                                      "Nadie se siente culpable por tu muerte porque eres un idiota que no sabe matemáticas, ella no te extraña nunca más.")

                            else:
                                print("\nNo presionas bien los caracteres. Mueres por idiota de un ataque al corazón.")

                        elif opcion == "n":
                            print("\nLa policia viene y te detiene. No la vuelves a ver nunca más ni a saber nada de ella. \n"
                                  "Todo ha terminado")

                        else:
                            print("\nTe quedas como idiota pensando una respuesta. Mueres por un ataque al corazón.\n"
                                  "NAdie quiere a un indeciso que no se detiene cuando las cosas llegan a los golpes. \n"
                                  "No a la violencia")

                    elif opcion == "n":
                        print("\nDecides no hacer nada.\n"
                              "Vuelves a casa después de un rato, pero ya no hay nada por hacer.\n"
                              "Ella se va a ir para siempre y no la vas a volver a ver.\n"
                              "Te suicidas después de un tiempo por ser un imbecil.")

                    else:
                        print("\nNo presionas la opción correcta y mueres por una bala perdida.\n"
                              "Ella se va con él porque ya no te quería. Nadie te extraña.")

                elif opcion == "b":
                    print("\nSales corriendo y te diriges a casa porque no quieres más problemas. Te sientes fatal\n"
                          "Te sientes inútil porque no pudiste defenderte, te sientes frustado, cansado y sin ganas de continuar.\n"
                          "En la subida a casa te encientras con tu chica que está con el sujeto odiado por ti.")
                    opcion = input("Ves que se despiden abrazandose… ¿Vas hacia el?\n"
                                   "S - Si\n"
                                   "N - No\n"
                                   "Opción: ")
                    opcion = opcion.lower()

                    if opcion == "s":
                        print("\nLlegas y lo golpeas, mientras ella se da cuenta. Tan desesperado te encuentras que solo quieres romperle las piernas. \n"
                              "Hace un momentop no te defendiste porque no querías problemas, pero esta vez los quieres y solo quieres golpearlo.\n"
                              "Te detienes al ver a la chica que amas, pero ellas se enoja y se va con él por lo que hiciste.\n"
                              "Ahora estás más solo que antes.")

                    elif opcion == "n":
                        print("\nEsperas a que ella llegue a casa y tú solo te quedas entado en el borde del precicpio esperando tener el valor para hacerlo")
                        opcion = input("¿Lo haces o solo regresas a casa?\n"
                                       "A - Hacerlo\n"
                                       "B - Regresar a casa\n"
                                       "Opción: ")
                        opcion = opcion.lower()

                        if opcion == "a":
                            print("\nFelicidades. Mueres siendo el coberda más grande que el mundo conoció. Ella se siente triste porque no sabe el motivo\n"
                                  "de tu decisión. Se siente culpable, pero al poco tiempo se recupera porque no es momento de estar triste por ti.\n"
                                  "Ella después de poco tiempo se vuelve la novia del chico y es más feliz que contigo")

                        elif opcion == "b":
                            print("\nVuelves a casa y te recuestas en sus brazos. Le cuentas lo que pasó y cómo te sentiste.\n"
                                  "El fúturo es incierto. Probablemente ella se va porque no es feliz contigo. \n"
                                  "Parece que al final te suicidaste.")

                        else:
                            print("\nNo presionaste la opción correcta. Un pajaro choca contigo y te empuja. Mueres al caer del puente y ser atropellado.")

                else:
                    print("\nNo eliges la opción adecuada. Te apuñala por la espalda un amigo del cholo.\n"
                          "Mueres y nadie te vuelve a ver. Los cholos orinan tu cuerpo")

        elif opcion == "s":
            print("\nEmpiezan a sonar canciones que alimentan tu odio hacia esa persona. Sólo quieres que no te quiten a la persona que más amas.")
            opcion = input("Te cuestionas lo que haces, te detienes y mejor te vas a casa. \n"
                           "¿Quieres tomar agua?\n"
                           "S - Si\n"
                           "N - No\n"
                           "Opción: ")

            if opcion == "s":
                print("\nBien hecho, el agua es lo mejor para ti.\n"
                      "Te acuestas en tu cama y esperas que todo mejore confiando siempre en ella… No será así, pero tú no lo sabes, quiérela mientras esté contigo. Es todo para nosotros.")

            else:
                print("\nEstá bien. Solo te acuestas y esperas que todo mejore confiando siempre en ella… No será así, pero tú no lo sabes, ámala mientras esté contigo. Es todo para nosotros.")
        else:
            print("\nNo presionaste una opción correcta. Te atropella un auto.")

    else:
        print("\nNo presionaste una opción correcta. Te asesina un cholo por pendejo")

elif opcion == "n":
    print("\nBien hecho, no es bueno leer estas cosas que salen de mi mente")

else:
    print("\nPor eso eres un pendejo. Ni presionar una tecla puedes hacer bien")