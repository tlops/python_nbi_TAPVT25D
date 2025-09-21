User Story
Som kund vill jag kunna beställa en pizza med toppings, så att jag får rätt totalpris.

Acceptanskriterier
En ny pizza kostar 80 kr.
Varje topping kostar 10 kr.
PizzaOrder("Margherita") utan extra toppings → 80 kr.
PizzaOrder("Margherita") med 2 toppings → 100 kr.
En pizza måste alltid ha minst en grund (ej tom order).

Övning
Börja med test för grundpris.
Lägg till test för toppings.
Lägg till test för felaktig order.
Använd pytest parametrisering för olika kombinationer.
