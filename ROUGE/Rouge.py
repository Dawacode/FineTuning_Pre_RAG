from rouge_score import rouge_scorer

def calculate_rouge_for_texts(reference_text, candidate_text):
    """Calculates ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L)."""
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_text, candidate_text)
    return scores

data = {
   "1": {
       "AI_Studio": "Byggnad: 4 800 000 kr. Mark: 3 200 000 kr. Anskaffningsutgiften för byggnad/mark (8 Mkr) fördelas enligt 19 kap. 11 § inkomstskattelagen (1999:1229) i proportion till taxeringsvärdena (byggnad 6 Mkr, mark 4 Mkr).",  
       "model": "Baserat på informationen i kontexten kan man inte exakt beräkna värdet av byggnaden respektive marken. Markens värde ska bestämmas utifrån marknadsvärdet under nivååret, och byggnadens värde utifrån marknadsvärdet."  
   },
   "2": {
       "AI_Studio": "Ja, beräkningen stämmer. Anskaffningsutgiften för byggnad och mark (8 000 000 kr) ska fördelas i proportion till taxeringsvärdena. Byggnadens andel blir (6 Mkr / 10 Mkr) * 8 Mkr = 4 800 000 kr. Markens andel blir (4 Mkr / 10 Mkr) * 8 Mkr = 3 200 000 kr, enligt 19 kap. 11 § inkomstskattelagen (1999:1229).",  
       "model": "Byggnaden ska bokföras till ett värde av 11 000 000 kr och marken ska bokföras till ett värde av 4 000 000 kr."  
   },
   "3": {
       "AI_Studio": "Offentlighetsprincipen innebär att allmänheten har rätt till insyn i myndigheters verksamhet.[1] Detta uttrycks genom rätten att ta del av allmänna handlingar, vilket regleras i 2 kap. tryckfrihetsförordningen (1949:105).",  
       "model": "Baserat på den tillhandahållna kontexten kan man inte ge en fullständig definition av \"offentlighetsprincip\". Istället finns det krav på öppenhet och transparens i olika sammanhang, särskilt inom offentlig upphandling, inkomsterätt och patentområdet, som återspeglar en underliggande princip om offentlighet." 
   }, 
   "4": {
       "AI_Studio": "Enligt svensk rättspraxis och doktrin kan skadeståndsansvar enligt aktiebolagslagen (2005:551) 29 kap. 1 § även omfatta de facto directors, det vill säga personer som faktiskt agerat som styrelseledamöter utan formellt uppdrag.[1][2][3][4][5][6] Detta ansvar förutsätter att de uppsåtligen eller av oaktsamhet skadat bolaget",
       "model": "Baserat på den angivna kontexten kan man säga att ABL fastställer skadeståndsansvar för styrelseledamöter, verkställande direktörer och aktieägare. “De facto directors”, dvs. individer som utför styrelsesysslor, kan hållas ansvariga om deras handlingar orsakar skada, under förutsättning att detta beror på uppsåt eller oaktsamhet. Aktieägare kan också hållas ansvariga i vissa fall. Domstolsavgöranden (NJA2006s136 & NJA2017s1101) illustrerar att skadeståndsansvaret bedöms utifrån konkreta omständigheter och bristerna i utförandet av uppgiften."
   },
   "5": {
       "AI_Studio": "Obeställd reklam regleras i marknadsföringslagen (2008:486). Enligt 21 § är det förbjudet att skicka obeställd reklam via e-post, sms eller liknande om mottagaren inte aktivt samtyckt till det. Undantag finns för befintliga kundrelationer.",
       "model": "Baserat enbart på informationen i kontexten, regleras obeställd reklam i Sverige genom Marknadsforingslag_MFL. Utan tillgång till själva lagtexten kan jag inte ge en detaljerad beskrivning av reglerna."
   },
   "6": {
       "AI_Studio": "Obeställd reklam regleras i marknadsföringslagen (2008:486). Enligt 21 § är det förbjudet att skicka obeställd reklam via e-post, sms eller liknande om mottagaren inte aktivt samtyckt till det. Undantag finns för befintliga kundrelationer.",
       "model": "Baserat på den angivna kontexten regleras obeställd reklam i Sverige genom Marknadsförringslagen (MFL)."
   },
   "7": {
       "AI_Studio": "Nej, en näringsidkare får inte använda vilseledande reklam. Enligt 10 § marknadsföringslagen (2008:486) är vilseledande marknadsföring otillbörlig om den påverkar eller sannolikt påverkar mottagarens förmåga att fatta ett välgrundat affärsbeslut.",  
       "model": "Baserat på den angivna kontexten får en näringsidkare inte använda vilseledande reklam. Detta följer av ett direkt förbud mot vilseledande marknadsföring och en näringsidkäres skyldighet att avråda."
   },
    "8":{
        "AI_Studio": "Lagen (1982:80) om anställningsskydd (LAS) reglerar uppsägning. Enligt 7 § LAS ska en uppsägning från arbetsgivarens sida vara sakligt grundad.",
         "model": "Kravet på att uppsägningen skall vara skriftlig samt innehållsförhållande gäller endast uppsägningar från arbetsgivarens sida. Detta reglerasi Lagen om anställningsskydd (LAS)."
    },
    "9":{
        "AI_Studio": "Rättegångsbalken (1942:740) är tillämplig.[1] Specifikt reglerar 2 kap. om hovrätt och 50-53 kap. rättegången i hovrätt i tvistemål, samt 51 kap. och 54-57 kap. rörande brottmål.",
         "model": "Baserat på den angivna kontexten är de lagar som är tillämpliga vid rättegång i hovrätten de lagar som beskriver tillämpningsområdet för respektive lag. Specifikt är detta brottsbalken (kapitlet om rättegång i hovrätt)."
    },

    "10":{
        "AI_Studio": "För misshandel av normalgraden är straffet fängelse i högst två år. Är brottet ringa döms till böter eller fängelse i högst sex månader. Detta framgår av 3 kap. 5 § Brottsbalken (1962:700).",
         "model": "Lägsta straffet för misshandel av normalgraden är troligen ett års fängelse. Högsta straffet för misshandel av normalgraden är högst sex år."
    },
    "11":{
        "AI_Studio": "Ja, det är i regel möjligt. En civil skadeståndstalan styrs av Skadeståndslagen (1972:207) och Rättegångsbalken (1942:740). Olika beviskrav gäller i brottmål jämfört med tvistemål, vilket är relevant för bedömningen (jfr principer i Rättegångsbalken, t.ex. 35 kap. 1 § om fri bevisprövning).",
         "model": "Baserat enbart på den tillhandahållna kontexten kan jag inte ge ett definitivt svar på frågan om man kan stämma en person för misshandel efter att domstolen har utfärdat ett ogillande dom. Kontexten innehåller ingen information som direkt adresserar detta scenario. Jag kan inte uttala mig om möjligheten att stämma."
    }


}


def pretty_print_rouge(rouge_scores):
    for metric, score in rouge_scores.items():
        print(f"    {metric.upper()}: P={score.precision:.2f}, R={score.recall:.2f}, F1={score.fmeasure:.2f}")

for question_num, answers in data.items():
    AI_Studio_answer = answers["AI_Studio"]
    model_answer = answers["model"]

    rouge_scores = calculate_rouge_for_texts(AI_Studio_answer, model_answer)

    print(f"\nQuestion {question_num}:")
    print(f"  AI Studio Answer: {AI_Studio_answer}")
    print(f"  Model Answer: {model_answer}")
    print("  ROUGE Scores:")
    pretty_print_rouge(rouge_scores)
