#!/usr/bin/python
import argparse
import random

parser = argparse.ArgumentParser(description='A hervorragender '
    +'Blindtextgenerator, nua midam Best\'n vom Freistoat, nämlich da '
    +'bairischn Sproch\'n! ')
parser.add_argument('--huife', action='store_true',
    help='Zeigt a die Huifn o, und macht danoch nix!')
parser.add_argument('-g', '--grantln', action='store_true', help='Normalweis'
    +' generiad des Tool a Schmarrn. So werd beleidigenda Schmarrn draus!')
parser.add_argument('-a', '--absaetz', type=int, default=4,
    help='Anzoi der Absätz, die des Tool generiat (Normalerweis fia)')
parser.add_argument('-l', '--laeng', type=int, default=20,
    help='Läng der Absätz (Anzoi der Wörta im Absotz), die generiat werd\'n'
    +' (Normalerweis zwoaßg)')
parser.add_argument('-o', '--oawort', action='store_true',
    help='Generiat nua oa woat. Mit --grantln wiads a Schimpfword!')

args = parser.parse_args()

grantl = ["Aff", "Affnasch", "Apruiaff", "Asphaltwanzn", "Aufgeiga", "aufgschdeida Mausdreg", "Aufmüpfiga", "Aufschneida", "Auftaklta", "Auftreiwa", "aus\'gschammta", "Aushuifsbaya", "Badhur", "Badwaschl", "Bagaasch", "Bauantrampl", "Bauernfünfa", "Bauernschädl", "Bazi", "Beißn", "Beißzanga", "Beitlschneida", "Besnbinda", "Betonschedl", "Betschwesta", "Bettbrunza", "Bettwanzn", "Biaschdal", "Bierdimpfl", "Bixlmadam", "Blasengl", "Blattada", "boaniga", "Bodschal", "Britschn", "Broatarsch", "Bruinschlanga", "Brunzer", "Brunzkachl, du ogsoachte", "bsuffas Wagscheidl", "Chaotngschwerl", "Charaktasau", "Daamaluudscha", "damischa Depp", "damischa Saupreiß", "depperta Doafdebb", "di hams midam Stickl Brot ausm Woid raußzogn", "Dickschedl", "Dipfalscheißa", "Doafdrottl", "Doafmatratzn", "Dramhappada", "dreckata Drek", "Dreeghamml", "Dreegsau", "Dreegschleida", "Drottl", "du Ams\'l, du bleede", "du bist doch af da Brennsuppn daheagschwomma", "du ogsoachte", "du saudamischa", "Duitaff", "Ecknsteha", "Eignbrödla", "eigschnabbda", "Eisackla", "elendiger", "Erzdepp", "fade Noggn", "Fechtbruada", "Fegeisen", "Fettl", "Fieschkoobf", "Finessenseppal", "Flaschn", "Flegel", "Fliedschal", "Freibialädschn", "Freindal", "Frichdal", "Fünferl", "Geizgroogn", "Gibskobf", "Gifthafal", "Giftschbridzn", "Gigal", "glei fangst a boa", "glei foid da Wadschnbam um", "Gmoadepp", "Goaspeterl", "Goggolore", "Grachal", "Grantla", "Grantlhuaba", "Grattla", "Grawurgl", "greißlicha Uhu", "Griasgram", "Griggalheudda", "Grischbal", "Großkopfada", "Gschaftlhuaba", "gscheada Saubreiß", "gscheate Ruam", "Gscheidal", "Gscheidhaferl", "gscherta Hamml", "gscherte Nuss", "Gschpusi", "gwampate Sau", "Halbkreisingeneur", "halbseidener", "Hallodri", "Hämmoridenpritschn", "Hampara", "Hanswurst", "Haumdaucha", "Hausdracha", "Heislmo", "Heislschlaicha", "Hemmadbiesla", "Herrgoddsacklzementfixlujja", "Himbeerdoni", "Himmeheagodna", "Himmi Herrgott Saggrament", "hindafozziga", "Hinderducker", "Hockableiba", "Hodalumb", "Hoibschaariga", "hoid dei Babbn", "hoit dei damische Goschn", "hoit\'s Mei", "Honigscheißa", "Hopfastanga", "Hornochs", "hosd mi", "Hosnscheissa", "Hubbfa", "Hundsbua", "Hundsgribbe", "Hungaleida", "i glaub, dir brennt da Huat", "i werd da zoagn, wo da Bartl an Most hoid", "i-Düpferl-Reita", "ja, wo samma denn", "Jochgeia", "junga Duttara", "junga Hubbfa", "Jungfa", "Kaasloabe", "Kamejtreiba", "Karfreidogsratschn", "Kasberl", "Kasberlkopf", "Katzlmacha", "Kirchalicht", "Kircharutschn", "Kittlschliaffa", "Klaubauf", "klebrigs Biaschal", "Klobürschdn", "Klugscheissa", "Knedlfressa", "Kniabisla", "Krampfhenna", "Krautara", "Kreizdeifi", "Krippnmandl", "kropfata Hamml", "krummhaxata Goaßbog", "Lätschnbebbi", "Lausbua", "Luada", "misdiga Lausbua", "Mistviach", "mit deinen Badwandlfüaß", "mogsd a Wadschn", "Nasnboara", "Neidhamml", "Oasch", "Oaschgsicht", "oida Daddara", "oida Daggl", "oida Schlawina", "oide Bixn", "oide Rudschn", "oide Schäsn", "oide Schäwan",
          "Palmesel", "Pfennigfuxa", "Pfingsdochs", "Pfundhamme", "Pfundhamml", "Pfundsau", "Pimpanell", "Plotschn", "Presssack", "Pritschn", "Rabenviech", "Radlfahra", "Randstoamare", "Ratschkathl", "Rotzgloggn", "Ruaßnosn", "Rutschn", "Sagglzemend", "Saggrament", "Sau", "Saubreiß, japanischer", "Saubreiß", "Saufbeitl", "Sautreiba", "Schachtlhuba", "Schanial", "schau, dass di schleichst", "Schbinodwachdl", "Schbringgingal", "Schbruchbeidl", "schdaubiga Bruada", "Schdeckalfisch", "Schdehlratz", "Schdinkadores", "Scheißbürschdl", "schiache Goaß", "Schlampnschleppa", "Schlawina", "schleich di", "Schleimscheißa", "Schnoin", "Schnointreiba", "Schoaßwiesn", "Schoaswiesn", "Schrumsl", "Schuasda", "Schuggsn", "Schuibuamtratza", "Schundnickl", "Schusterbua", "Schwammal", "Schwindsüchtl", "Schwobndeifi", "Schwobnsäckle", "Spinotfressa", "Stodara", "Umstandskrama", "varreckta Deifi", "varreckter Hund", "Vieh mit Haxn", "Voglscheicha", "Voiksdepp", "Woibbadinga", "Wuidsau", "Wurznsepp", "Zeeefix", "Zefix, no amoi", "Zigarettnbiaschal", "Zipfebritschn", "Zuagroasta", "Zuchtl", "Zwedschgarl", "Zwedschgndatschi", "Zwedschgnmanndl", "Zwidawurzn"]
schmarrn = ["a", "a bissal", "a bissal wos gehd ollaweil", "a bravs", "a fescha Bua", "a ganze", "a ganze Hoiwe", "a geh", "a Hoiwe", "a liabs Deandl", "a Maß und no a Maß", "a Prosit der Gmiadlichkeit", "a so a Schmarn", "aasgem", "aba", "abfieseln", "af", "allerweil", "Almrausch", "am acht\'n Tag schuf Gott des Bia", "amoi", "an", "anbandeln", "auf der Oim, da gibt\'s koa Sünd", "auf\'d Schellnsau", "auf gehds beim Schichtl", "auffi", "Auffisteign", "auszutzeln", "Baamwach", "back mas", "baddscher", "barfuaßat", "Biagadn", "Biakriagal", "Biawambn", "Biaschlegl", "Biazelt", "bitt", "bittschön", "Bladl", "blärrd", "Blosmusi", "boarischer", "Bradwurschtsemmal", "Breihaus", "Brezn", "Broadwurschtbudn", "Brodzeid", "Brotzeit", "Buam", "Bussal", "Charivari", "d\'", "da", "da", "da Kini", "da, hog di hi", "dahoam", "dahoam", "damischa", "de", "de Sonn", "Deandlgwand", "ded", "dei", "des", "des basd scho", "des is a gmahde Wiesn", "des is hoid aso", "des is schee", "des muas ma hoid kenna", "des wiad a Mordsgaudi", "di", "Diandldrahn", "do", "do", "do legst di nieda", "dringma aweng", "du dadst ma scho daugn", "eam", "eana", "ebba", "Edlweiss", "Engelgwand", "Enzian", "es", "etza", "Ewig und drei Dog", "fei", "fensdaln", "fias", "Fingahaggln", "Foidweg", "Freibia", "Fünferl", "g\'hupft wia gsprunga", "Gams", "Gamsbart", "gar nia need", "Gaudi", "geh", "gelbe Rüam", "gfreit mi", "ghupft wia gsprunga", "Gidarn", "glacht", "glei", "Goaßmaß", "gor", "Graudwiggal", "greaßt eich nachad", "Greichats", "griasd eich midnand", "Griasnoggalsubbm", "griaß God beinand", "großherzig", "gscheckate", "gscheid", "gscheit", "Gschicht", "gschmeidig", "Gstanzl", "guad", "Guglhupf", "gwihss", "gwiss", "gwiss", "Habedehre", "Haberertanz", "Haferl", "hallelujah sog i, luja", "ham", "hawadere midananda", "hea", "heid", "heid gfoids ma sagrisch guad", "Heimatland", "heitzdog", "helfgod", "Hemad", "Hendl", "Hetschapfah", "hi", "hinter\'m Berg san a no Leit", "hoam", "hob", "hob i an Suri", "hod", "hod", "hogg di hera", "hogg ma uns zamm", "hoggd", "hoid", "i", "i", "i bin a woschechta Bayer", "i daad", "i hab an", "i hob di liab", "i hob di narrisch gean", "i mechad dee Schwoanshaxn", "i moan scho aa", "i moan oiwei", "i mog di fei", "i sog ja nix, i red ja bloß", "i waar soweid", "iabaroi", "im Beidl", "imma", "in da", "in da greana Au", "is", "is", "is des liab", "is ma Wuascht", "ja, wo samma denn", "jedza", "jo leck mi", "jo mei", "jo mei is des schee", "Jodler", "Kaiwe", "kimmt", "kimmt", "Kirwa", "Klampfn", "kloan", "Kneedl", "koa", "Kuaschwanz", "kumm geh", "kummd", "Landla", "Ledahosn", "lem und lem lossn", "Leonhardifahrt", "Lewakaas", "liberalitas Bavariae", "luja", "ma", "Maderln", "Maibam", "Mamalad", "Marei", "Marterl", "Maßkruag", "measi", "mechad", "mehra", "mei", "Meidromml", "mi", "midanand", "middn", "Milli", "mim", "mim Radl foahn", "moand", "mogsd a Bussal", "Mongdratzal", "muass", "Musi", "naa", "naa", "nackata", "Namidog", "ned",
            "ned", "ned woar", "nia need", "nia need", "nimma", "nimmds", "nia", "nix", "nix Gwiass woass ma ned", "no", "no a Maß", "noch da Giasinga Heiwog", "nomoi", "o\'ha", "oa", "Oachkatzlschwoaf", "oamoi", "oans", "oans, zwoa, gsuffa", "oba", "obacht", "obandeln", "obandln", "Obazda", "ognudelt", "Ohrwaschl", "nois", "om auf\'n Gipfe", "owe", "ozapfa", "pfenningguat", "pfiad de", "pfundig", "Prosd", "Radi", "Radler", "Ramasuri", "Reiwadatschi", "resch", "resch", "Resi", "samma", "sammawiedaguad", "san", "Sauakraud", "sauba", "Sauwedda", "schaugn", "Schaung kost nix", "Schbozal", "Schdarmbeaga See", "Schdeckalfisch", "scheans", "Schmankal", "Schneid", "Schorsch", "schoo", "Schuabladdla", "schüds nei", "sei", "Semmlkneedl", "Sepp", "Servas", "singan", "singd", "schnacksln", "so", "so schee", "sodala", "sog i", "sog i", "soi", "sowos", "spernzaln", "Spezi", "Spuiratz", "Spotzerl", "Steckerleis", "Stubn", "Trachtnhuat", "trihöleridi dijidiholleri", "um Godds wujn", "umananda", "umma", "unbandig", "und", "und glei wirds no fui lustiga", "und sei", "vasteh", "Vergeltsgott", "vo de", "von", "vui", "vui huift vui", "wann griagd ma nacha wos z\'dringa", "Watschnbaam", "Watschnpladdla", "wea ko, dea ko", "wea nia ausgähd, kummt nia hoam", "Weibaleid", "weida", "Weißwiaschd", "Weiznglasl", "wia", "wia da Buachbinda Wanninger", "wiavui", "Wiesn", "wo hi", "woaß", "Woibbadinga", "wolln", "wolpern", "wos", "wos", "wui", "wuid", "Wurscht", "Wurschtsolod", "Xaver", "Zidern", "zua", "zünftig", "Zwedschgndadschi", "zwoa"]

def random_word(words):
    x = random.randint(0, len(words)-1)
    return words[x]

def text_generator(words, length, paragraphs, seperator):
    text = ''
    paragraph = ''
    for i in range(paragraphs):
        for j in range(length-1):
            paragraph += random_word(words) + seperator
        paragraph += random_word(words) + random_word([".", "!", "?"])
        if i < paragraphs-1:
            paragraph += ' \n\t'
        paragraph = paragraph[0].upper() + paragraph[1:]
        text += paragraph
    return text

if args.huife:
    parser.print_help()
elif (args.grantln):
    # grantln generation
    if args.oawort:
        print(random_word(grantl))
    else:
        print(text_generator(grantl, args.laeng, args.absaetz, ", "))
else:
    # schmarrn generation
    if args.oawort:
        print(random_word(schmarrn))
    else:
        print(text_generator(schmarrn, args.laeng, args.absaetz, " "))
