def lookup_static_data(track):
    #TODO - change to ordered lists
    staticTrackData = {
        'A1-Ring':{'wings':332,'engine':773,'brakes':675,'gear':802,'susp':553},
        'Adelaide':{'wings':624,'engine':528,'brakes':369,'gear':560,'susp':719},
        'Anderstorp':{'wings':367,'engine':725,'brakes':778,'gear':622,'susp':199},
        'Avus':{'wings':451,'engine':681,'brakes':435,'gear':243,'susp':873},
        'Baku City':{'wings':533,'engine':649,'brakes':747,'gear':680,'susp':933},
        'Barcelona':{'wings':488,'engine':721,'brakes':509,'gear':684,'susp':368},
        'Brands Hatch':{'wings':517,'engine':686,'brakes':390,'gear':723,'susp':705},
        'Brasilia':{'wings':610,'engine':594,'brakes':612,'gear':810,'susp':938},
        'Bremgarten':{'wings':849,'engine':561,'brakes':694,'gear':526,'susp':537},
        'Brno':{'wings':530,'engine':530,'brakes':390,'gear':577,'susp':550},
        'Buenos Aires':{'wings':860,'engine':543,'brakes':280,'gear':668,'susp':775},
        'Estoril':{'wings':492,'engine':710,'brakes':310,'gear':725,'susp':644},
        'Fiorano':{'wings':499,'engine':815,'brakes':259,'gear':334,'susp':998},
        'Fuji':{'wings':360,'engine':630,'brakes':645,'gear':706,'susp':571},
        'Grobnik':{'wings':631,'engine':331,'brakes':595,'gear':805,'susp':563},
        'Hockenheim':{'wings':486,'engine':687,'brakes':331,'gear':804,'susp':349},
        'Hungaroring':{'wings':830,'engine':440,'brakes':584,'gear':448,'susp':480},
        'Imola':{'wings':486,'engine':624,'brakes':675,'gear':622,'susp':495},
        'Indianapolis':{'wings':314,'engine':781,'brakes':481,'gear':658,'susp':585},
        'Interlagos':{'wings':507,'engine':617,'brakes':565,'gear':582,'susp':393},
        'Irungattukottai':{'wings':647,'engine':484,'brakes':637,'gear':633,'susp':595},
        'Istanbul':{'wings':450,'engine':570,'brakes':712,'gear':558,'susp':701},
        'Jerez':{'wings':690,'engine':613,'brakes':640,'gear':712,'susp':401},
        'Jyllands-Ringen':{'wings':827,'engine':339,'brakes':650,'gear':661,'susp':537},
        'Kyalami':{'wings':925.5,'engine':661,'brakes':588,'gear':321,'susp':838},
        'Laguna Seca':{'wings':528,'engine':390,'brakes':603,'gear':638,'susp':129},
        'Magny Cours':{'wings':495,'engine':599,'brakes':316,'gear':608,'susp':631},
        'Melbourne':{'wings':450,'engine':674,'brakes':625,'gear':770,'susp':375},
        'Mexico City':{'wings':633,'engine':755,'brakes':476,'gear':686,'susp':400},
        'Monte Carlo':{'wings':925,'engine':355,'brakes':481,'gear':388,'susp':568},
        'Montreal':{'wings':395,'engine':738,'brakes':583,'gear':737,'susp':281},
        'Monza':{'wings':240,'engine':800,'brakes':505,'gear':883,'susp':680},
        'Mugello':{'wings':550,'engine':823,'brakes':886,'gear':910,'susp':680},
        'Nurburgring':{'wings':644,'engine':445,'brakes':641,'gear':606,'susp':207},
        'Oesterreichring':{'wings':464,'engine':707,'brakes':500,'gear':752,'susp':649},
        'Paul Ricard':{'wings':446,'engine':988,'brakes':157,'gear':647,'susp':818},
        'Poznań':{'wings':701,'engine':557,'brakes':390,'gear':731,'susp':617},
        'Sakhir':{'wings':211,'engine':390,'brakes':731,'gear':623,'susp':302},
        'Sepang':{'wings':582,'engine':623,'brakes':668,'gear':761,'susp':505},
        'Serres':{'wings':878,'engine':504,'brakes':513,'gear':297,'susp':663},
        'Shanghai':{'wings':486,'engine':556,'brakes':648,'gear':379,'susp':190},
        'Silverstone':{'wings':369,'engine':756,'brakes':605,'gear':825,'susp':482},
        'Singapore':{'wings':820,'engine':440,'brakes':585,'gear':618,'susp':869},
        'Spa':{'wings':601,'engine':728,'brakes':445,'gear':612,'susp':461},
        'Suzuka':{'wings':451,'engine':681,'brakes':526,'gear':562,'susp':562},
        'Valencia':{'wings':747,'engine':471,'brakes':663,'gear':635,'susp':371},
        'Yas Marina':{'wings':754,'engine':465,'brakes':559,'gear':492,'susp':476},
        'Yeongam':{'wings':772,'engine':493,'brakes':727,'gear':702,'susp':472},
        'Zandvoort':{'wings':579,'engine':706,'brakes':423,'gear':794,'susp':766},
        'Zolder':{'wings':674,'engine':653,'brakes':470,'gear':636,'susp':599},
        'Indianapolis Oval':{'wings':82,'engine':735,'brakes':38,'gear':847,'susp':305},
        'New Delhi':{'wings':647,'engine':580,'brakes':560,'gear':739,'susp':184},
        'Bucharest Ring':{'wings':383,'engine':686,'brakes':772,'gear':575,'susp':792},
        'Ahvenisto':{'wings':946,'engine':476,'brakes':708,'gear':777,'susp':286},
        'Portimao':{'wings':789,'engine':388,'brakes':485,'gear':505,'susp':352},
        'Kaunas':{'wings':445,'engine':681,'brakes':516,'gear':704,'susp':431}
    }
    trackDataInput = f'{track}'
    trackData = staticTrackData[trackDataInput]
    partData = {
        'wings':[4.5,-0.45,-0.75,35.7,-9.9,-12.9,4.0,207],
        'engine':[-3.75,-0.5,0.3,0.77,16,8.2,4.59,-231],
        'brakes':[5.9,0.65,-0.5,-28.6,8.0,-1.915,102],
        'gear':[-4.2,1.05,0.45,-41.5,9.0,-3.835,-8.7],
        'susp':[-6.0,-0.5,0.76,1.54,34.8,-17.0,-10.0,5.2,-249]
    }
    
    return trackData,partData

def lookup_tyre_suppliers(tyreId):
    
    tyreSuppliers = {
        '1': 'Pipirelli',
        '9': 'Avonn',
        '2': 'Yokomama',
        '3': 'Dunnolop',
        '8': 'Contimental',
        '4': 'Badyear'
    }
    tyreSupplier = tyreSuppliers[f'{tyreId}']
    
    return tyreSupplier