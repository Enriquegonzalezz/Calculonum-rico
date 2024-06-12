
nombre <- readline(prompt="holiss como te llamas:" )
  numero1 <- as.integer(readline(prompt=paste("Hola", nombre, "ahora dime un número: ")))
 numero2 <- as.integer(readline(prompt=paste("vale ahora necesito otro: ")))
 numero2 <- as.integer(numero2)
 resultado <- numero1 + numero2
 print(paste("la suma de ellas: ", resultado))
