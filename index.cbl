       
       
       IDENTIFICATION DIVISION.

       PROGRAM-ID. CAL-TAX.
           
       DATA DIVISION.

       FILE SECTION.

       WORKING-STORAGE SECTION.

       01 ENTRADA PIC 9(9)V99.

       01 IMPUESTOS PIC ZZZZZZZZZ9.99.

       PROCEDURE DIVISION.

       MAIN-PROCEDURE.

           PERFORM INICIO.

           PERFORM ACEPTA-NUMERO.

           PERFORM MUESTRA-RESULTADO.

           PERFORM OTRO-NUMERO WITH TEST AFTER UNTIL ENTRADA = 0.

           PERFORM FIN.
       INICIO.

           DISPLAY 'INTERODUCE TUS INGRESOS ANUALES: '.

       ACEPTA-NUMERO.

           ACCEPT ENTRADA.

       MUESTRA-RESULTADO.

           IF ENTRADA > 100000

           COMPUTE IMPUESTOS = (ENTRADA * 10) / 100

           DISPLAY "ESTE ANO TIENES QUE PAGAR : " IMPUESTOS

           ELSE

           DISPLAY 'NO TIENES QUE PAGAR IMPUESTOS '

           END-IF

           DISPLAY 'INTRODUCE OTRO INGRESO O PULSA 0 PASA SALIR '.

       OTRO-NUMERO.

           PERFORM ACEPTA-NUMERO

           IF ENTRADA = 0

           PERFORM FIN

ELSE

           PERFORM MUESTRA-RESULTADO

           END-IF.

       FIN.

           DISPLAY 'FIN DE PROGRAMA'

           STOP RUN.
