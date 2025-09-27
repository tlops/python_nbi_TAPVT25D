# Examinationsuppgift: Tärningsspelet 21

## Beskrivning
Du ska implementera ett textbaserat spel där användaren möter datorn i en förenklad variant av Blackjack.  
Målet är att komma så nära 21 poäng som möjligt utan att gå över.

Spelet går till så här:
1. Spelaren får välja om hen vill **rulla tärningen** (värde 1–6) eller **stanna**.
2. Om spelaren får över 21 förlorar denna direkt.
3. När spelaren stannar tar dealern (datorn) sin tur:
   - Dealern slår automatiskt tills den når minst 17 poäng.
   - Om dealern får över 21 vinner spelaren.
4. Om varken spelaren eller dealern får över 21 vinner den som är närmast 21.
5. Vid lika poäng blir det oavgjort.

## Kravspecifikation

Du får använda dig av bibliotek men se till att du har med en requirements.txt i så fall med alla bibliotek du använder.

### Kriterier för godkänt:
- Programmet ska:
  - Fråga spelaren om denna vill rulla eller stanna.
  - Visa resultatet av varje slag och nuvarande total.
  - Hantera att spelaren kan kan få över 21 och då förlorar.
  - Låta dealern spela enligt regeln: slå tills minst 17.
  - Avgöra och skriva ut vinnaren.
  - Det ska gå och spela igen.
  - Ha med **felhantering** om användaren skriver in ogiltigt val.

### Kriterier för Väl Godkänt:
- Allt i godkänt.
- Använda **klasser** för att modellera spelare och spelet.
- Implementera en **highscore**-funktion:
  - Räkna antal vinster för spelare respektive dealer.
  - Visa ställningen efter varje runda.
  - Detta ska sparas i fil på datorn som läses in vid start och sparas när spelet avslutas.
- Du ska även ha gjort några (minst 3) tester för ditt spel (du behöver inte ha gjort för allt) och motivera varför du har skrivit dina tester som du gjort och vad du vill testa. Detta kan du skriva som kommenterar i anslutning till testerna.

## Inlämning

Inlämning sker på Github och Learnpoint senast **söndag 28/9 kl 23:59**. Du ska lämna in en länk till ditt Github-repo med allt din kod på Learnpoint. Glöm inte och kolla så att ditt repo är publikt. På Learnpoint kan du lämna in länken antingen som en kommentar eller i en textfil som du laddar upp Learpoint. Texfilen ska i så fall ha ditt namn som namn ex. *christoffer-wallenberg.txt*. Allt kod behöver finnas i ditt Github-repo och projektet ska kunna köras utan fel för att kunna bli godkänt..
