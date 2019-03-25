import itertools
import gmpy2
import tqdm


def add(a, b, n):
    if a == 0:
        return b
    if b == 0:
        return a
    l = ((b[1] - a[1]) * gmpy2.invert(b[0] - a[0], n)) % n
    x = (l * l - a[0] - b[0]) % n
    y = (l * (a[0] - x) - a[1]) % n
    return (x, y)


def double(a, A, n):
    if a == 0:
        return a
    l = ((3 * a[0] * a[0] + A) * gmpy2.invert(2 * a[1], n)) % n
    x = (l * l - 2 * a[0]) % n
    y = (l * (a[0] - x) - a[1]) % n
    return (x, y)


def multiply(point, exponent, A, n):
    r0 = 0
    r1 = point
    for i in bin(exponent)[2:]:
        if i == '0':
            r1 = add(r0, r1, n)
            r0 = double(r0, A, n)
        else:
            r0 = add(r0, r1, n)
            r1 = double(r1, A, n)
    return r0


pairs = [
    # ...
    (
        116402452666072936208815007139304987216714163049811234781351426326924131246364364574334524817901508281619972460090415001382062843182592379805224835760303284979302327894596365679847657301006500492449662907010259006597668640036494093690719721777196202708412690708189425416261338322878726801565837339906926442199,
        65537),
    (
        72128528351313473420179314572119990604651270437592829193391256285705990511101289865986271523217360211474708035488775690482561674639104763764292816682698922237019191511464487193970754386110524879193694264393694735699397861685866957886245941323956784903309420884407300597875442332448856957254910545532821889299,
        65537),
    (
        73618876433004249184978145767172783337037825119797776152361817923664817235074266764755714712861070055072066803855856685111144102664346032049418668608287795534794538810875171762480060503166831962241494787605416017055880622029734994044932217821789153301768574125944415193646357008710302950483305389221066847901,
        65537),
    (
        73177321447605094844869475236452612124978534257135914699558017401422185626292715437598924702135960009348349691300480285412291444130014147979466710606556340281835123929389068816250814192724388565641377589583657874123204050726861623197564010221304135373073693842338290035929101006802541072441280400654249703501,
        65537),
    (
        97382797353045331646505494348654763629695118500138939883233433357428093757720771502472932547778170423520279098578548122465990700230382918476305807288169110329196315830396848939947866149803340899454247342824343067095662473924285853564075616336253637134238080736018128872667522917427064919655548196404869756027,
        65537),
    (
        67976197154503824252962758605192194537953455525684128171733591254402803175166581383475047847861663641713765757931682973068658192496297048845113783704321821755367088609853548033974113545899159802253261684992108321544814827090618620826695197738464245366135069431667050573287256082799616410638317073782521185023,
        65537),
    (
        110275897141076818271072096590513112897929955440068495493135515543092550627534271627915186797154186031156669060269702741611753123555487415805236788428089217775154900745490634263247868952528637709533999002473335659899799916937849685340491762097907881267967856293987095111816596080222558533051866152901772125021,
        65537),
    (
        123057907917436127539527907099425342475570330289265864158827525873310417371936928434895347441344811844300963731368763658252023935259953079856185113158366035547184680371892392991206818845224739890627054487438274464628358389953364889396328148337794864532496751214808274331285251973125187047444874919216099841871,
        65537),
    (
        49908311276352626867987101266653733677443922860417336220034713320042273876656140638566243873537821187354594266196560454702978329981116231532173256631459485155012546874109305140536203556215594155212381163348910193461364267170043591140543359285420953285587571782910900590740365863047751629303062068182008958447,
        65537),
    (
        157913681988511499223609035411981820911271233555707504083664130320290519024435979679403867737167438404145916472057724664284957996829571508983693318203378659748119970975665003836383147439301141526359886862434947265335155286657190682579048049590022337203836302341519460071474846004720235996086653421254947765763,
        65537),
    (
        130686364437650269192698818823451311084025541967821443000348384106399176937553017580087805965647877171871679318678086712702402219040050553097221918077061071767150713229500958984702583696138306241835397036226770025174584861960483672166855143240442388067296906085889597273547497384707457725785567051697620288591,
        65537),
    (
        98447025559940925232827050931888121526036906765539231848755409007026290227697917504072798230241827515905654264101758792557264835713951508032148586868604301557992353974382767950487795377771857505013585229566772858342910003450748215534545315409987783372787710467093839107349037532325869053036936439915995000667,
        65537),
    (
        128148111175823352400462319805160929115996482855537302608188848856115718867473093938595331878106244359323570786265749034905618595139132632591445847012279583359245356050448000736798205400593852565062720548334698821337574055248257689950607177156911416062014722135480340362989852670221941481886013770136850751781,
        65537),
    (
        60133710099569481953219733936355185497843685269798966661526559485888088964806657723669164097620106601394470774914652784368846237250490097224813901048798471457949043241739938530488909237738353283083272441572780068774355326365593076939566996768702710260435492005911366336238371920302826154596302489591346937117,
        65537),
    (
        132296050110897272334339998820605562636329015069015533767470479357350219249289057838530025206834894293739406130049933964211831294419072040144541695497664399405999938388606716123361623882351402180870306227491182637756842162486249491235751392480389809303781435608957403832447951953698844340067583897270426098451,
        65537),
    (
        60443967447785393138864178942366387651267156706414100121308602703368238345988508740905972277606852572017154817055737121571763014359104203111309689366934871164845704653432191423293137312866452247127470094627731047782391919349252045761903093568940111624321917870715297268881080867388146043384315838410915463867,
        65537),
    (
        136918206370524932086262079679496249278883042667036863127641001637706525334407484473524303122382386946747171360700704658418091837642370996924889244922836996980549871995108243992471926381284280555063732794779196088883946141172028949564769371108000421641872213648535721217813140890609181166662207662082348704031,
        65537),
    (
        102367317908137146899968063711512379914123164164576819234979076494060875710628883190426756245752623025408390955326022913655680823315841936756717557576129533565208189636315164057974978818161693652834151987365149323813077092749375518387232199256317441189779228807199187831234013566030596441666283949686905077073,
        65537),
    (
        145934577603596902789123407585129432891113775741400347792957078764620678896869519027591183553916285448325899194046748300141452107380867045766079342284941974686719082915846571763997200135729281754947047537461265063933657946633608923340609747852466911765527541852267183246775254549496116011666824081226894151711,
        65537),
    (
        146196365199763527772801351598930179444798935405378127149498390543551061500184881573295241678829701966661285430629709825662168346137118728044899407390251656452054238220687307329458824023952540116543126508715186509848862934290538224881044401349377667876630383226710763313619228403564829652819744281354999091947,
        65537),
    (
        95599169705445329592701275510692039025543533050944596476115282391996500522674739049577601836622448563615066729000974308473909772541547342158362913055440055291401497652027077723035596604407273198661322392402403664999687528845882326107542200934885510337640280522467705511212570922193258029913966888341705942657,
        65537),
    (
        88509941082990217821394023784713206714874995048091665689471761835332677023258162658550128225712497284395237650697242312294524983099697200660199729764030817196925399259057797933054297627737840573132994164423139734415316805296327386916295821604629007029939724521323927071950696025812048912504600260519528803017,
        65537),
    (
        134111500831101681888084662096822897930443451471325458092798353224754034989576978615857647339887611801658914818467942811429898123477859871351925743818919850778748749853737737368683794924655722326216626998647918889347810696535840188385184928160389460393973282546047548735063161727655098336855667384242359598681,
        65537),
    (
        130306222060725060856602382175523892980470512653246350073075580806662730679557557277464374502961018134085441212620057016628524818386266323364677166176951894987360048639581695566252534442476475281686881857138067703179217821345500952576114615041291709664412217664913072326196915640030302737664203101757972292009,
        65537),
    (
        109195968070181320039044527981737677734685200415259874176720395261789493474595972066369117732934653462393425853391113051919979196131805887787156088506977054069142613595836517632263488826103442442154133090995850836350780297830394824875047916712143502070733292931932032321399790061816364089259150785740520442229,
        65537),
    (
        74607405690539886321935591687907746809985636424282785838241035788521374937334947849309748381592437710590822285557051766591417305699032403010585704748635256461923204412267889662556523422202872084833018777879240366224590513411131027258751267422649780007455027747520198527780623987770176299740594991685357203173,
        65537),
    (
        91090156809815356112452078167687701730542171751162682410506549507495786301901107518042567116544711142223761207388679694578400110477668036139709442797146978675659710667809231214124066411614199551979403818038627252190358700147018411953687380947379407447922216464481772714136469640345216305034232582586562365917,
        65537),
    (
        131315163096219896758812319752056689254888786607563046633060320506820131297826433621647565558853405931809041045107818053632556000808023296764459662011108829868710926973389975732138751753033905128824386561725719043848924886547337294484850822351051691689516131843649850151431113221981757498388355691928621480351,
        65537),
    (
        133723158739377682399692563059966474724840073276549108594822890091933565795964545111214577690253117712756372514601082730042600416990789925947272276521761975705620608706327012384023728557517331912721216062843455859937500732234294440205368176717460231815476583510552104399148142342459637993705037765251544006207,
        65537)]


def find_repeat_p_or_q():
    for pair in tqdm.tqdm(itertools.combinations(pairs, 2)):
        if gmpy2.gcd(gmpy2.mpz(pair[0][0]), gmpy2.mpz(pair[1][0])) != 1:
            print(pair)


# ((145027482789690990262517750951541446221552255560520228703877313431483316741269117323705124775232890171059397344533125793378274261538984168613648947111600523237940505464340771538677343847823054950559536582762094561232606689017946799356626447164268129816358964385649508992872978250974645830516100018108294421843, 65537),

# (116402452666072936208815007139304987216714163049811234781351426326924131246364364574334524817901508281619972460090415001382062843182592379805224835760303284979302327894596365679847657301006500492449662907010259006597668640036494093690719721777196202708412690708189425416261338322878726801565837339906926442199, 65537))


if __name__ == '__main__':
    # find_repeat_p_or_q()
    n = gmpy2.mpz(
        145027482789690990262517750951541446221552255560520228703877313431483316741269117323705124775232890171059397344533125793378274261538984168613648947111600523237940505464340771538677343847823054950559536582762094561232606689017946799356626447164268129816358964385649508992872978250974645830516100018108294421843)
    p = gmpy2.gcd(
        gmpy2.mpz(
            145027482789690990262517750951541446221552255560520228703877313431483316741269117323705124775232890171059397344533125793378274261538984168613648947111600523237940505464340771538677343847823054950559536582762094561232606689017946799356626447164268129816358964385649508992872978250974645830516100018108294421843),
        gmpy2.mpz(
            116402452666072936208815007139304987216714163049811234781351426326924131246364364574334524817901508281619972460090415001382062843182592379805224835760303284979302327894596365679847657301006500492449662907010259006597668640036494093690719721777196202708412690708189425416261338322878726801565837339906926442199))
    q = n // p
    e = 65537
    c = (
        gmpy2.mpz(
            84876076421614376067149365902722288787017939432560112310344060253776893355155004799570079133487890091744927361496759572955051910756381500540609425582325044679541917701176783432330786945586473421496533459046926087433374002572145804591821522550941784213497101941864710192882108942428579695906987627994038160506),
        gmpy2.mpz(
            53075793789885196175396474745354653894462035118379186161754018180061911263633656154635135006901226712322309187026865430527729260554951872682683031998933681813562644904853338601687712543027240467179318352856177931746928027694032725413016073749325323908751643659718884095101708806519753380797321211563244283733))
    lcm = gmpy2.lcm((p + 1), (q + 1))
    d = gmpy2.invert(e, lcm)

    p0, p1 = multiply(c, d, 0, n)
    print(hex(p1 - p0))
    # ASIS{58cf105e8993ff852a7ea69c3f6464458a87c69f89ef3dfd749da4e2d3982de34832e38cab1baf8d1cd3ce0f73251629}