import random, time, keyboard

autostop = 1

if __name__ == "__main__":
    class RNG:
        def __init__(self, items, probabilitySum, itemsProbability, itemsName, rollsCounter):
            self.items = items
            self.probabilitySum = probabilitySum
            self.itemsProbability = itemsProbability
            self.itemsName = itemsName
            self.rollsCounter = rollsCounter

    SQZsRNG = RNG({
                'Common - 1 in 2 (50%)': 5000000,
                'Uncommon - 1 in 4 (25%)': 2500000,
                'Rare - 1 in 8 (12,5%)': 1250000,
                'Special - 1 in 20 (5%)': 500000,
                'Bronze - 1 in 33 (3,3%)': 330000,
                'Epic - 1 in 50 (2%)': 200000,
                '-Legendary- \n 1 in 100 (1%)': 100000,
                '-Silver- \n 1 in 200 (0,5%)': 50000,
                '-MYTHIC- \n 1 in 500 (0,2%)': 20000,
                '\n -=DIABOLI=- \n 1 IN 1,000 (0,1%) \n': 10000,
                '\n -=SMOOTH=- \n 1 IN 1,000 (0,1%) \n': 10000,
                '\n -=LEGENDARY: SPECIAL=- \n 1 IN 1,000 (0,1%) \n': 10000,
                '\n -=GOLDEN=- \n 1 IN 2,000 (0,05%) \n': 5000,
                '\n -=MAGNETIC=- \n 1 IN 2,500 (0,04%) \n': 4000,
                '\n -=HOLY=- \n 1 IN 5,000 (0,02%) \n': 2000,
                '\n -=PROFANED=- \n 1 IN 5,000 (0,02%) \n': 2000,
                '\n\n --==(UNDEAD)==-- \n 1 IN 10,000 (0,01%) \n\n': 1000,
                '\n\n --==(PLATINUM)==-- \n 1 IN 10,000 (0,01%) \n\n': 1000,
                '\n\n --==(GLACIER)==-- \n 1 IN 10,000 (0,01%) \n\n': 1000,
                '\n\n --==(SIDEREUM)==-- \n 1 IN 10,000 (0,01%) \n\n': 1000,
                '\n\n --==(EPILEPTIC)==-- \n 1 IN 20,000 (0,005%) \n\n': 500,
                '\n\n --==(UNIQUE)==-- \n 1 IN 20,000 (0,005%) \n\n': 500,
                '\n\n --==(GOLD: ROSE GOLD)==-- \n 1 IN 20,000 (0,005%) \n\n': 500,
                '\n\n --==(SOLAR)==-- \n 1 IN 25,000 (0,004%) \n\n': 400,
                '\n\n --==(LUNAR)==-- \n 1 IN 25,000 (0,004%) \n\n': 400,
                '\n\n --==(NAUTILUS)==-- \n 1 IN 50,000 (0,002%) \n\n': 200,
                '\n\n --==(EXOTIC)==-- \n 1 IN 50,000 (0,002%) \n\n': 200,
                '\n\n\n\n _---==={CHROMATIC}===---_ \n\n 1 IN 100,000 (0,001%) \n\n\n\n': 100,
                '\n\n\n\n _---==={ARCANE}===---_ \n\n 1 IN 200,000 (0,0005%) \n\n\n\n': 50,
                '\n\n\n\n _---==={NULL}===---_ \n\n 1 IN 200,000 (0,0005%) \n\n\n\n': 50,
                '\n\n\n\n _---==={SOLAR & LUNAR: SOLAR ECLIPSE}===---_ \n\n 1 IN 250,000 (0,0004%) \n\n\n\n': 40,
                '\n\n\n\n _---==={HYPER-ELECTRIC}===---_ \n\n 1 IN 500,000 (0,0002%) \n\n\n\n': 20,
                ####################
                '''\n\n\n\n
                ╦╔╦╗╔╦╗╔═╗╦═╗╔╦╗╔═╗╦  
                ║║║║║║║║ ║╠╦╝ ║ ╠═╣║  
                ╩╩ ╩╩ ╩╚═╝╩╚═ ╩ ╩ ╩╩═╝
                
                1 IN 1,000,000 (0,0001%)
                \n\n\n\n''': 10,
                ####################
                '''\n\n\n\n
                 ___      __  ___    __            ___  __   ___       __        __      
                |__  \_/ /  \  |  | /  ` .   |    |__  / _` |__  |\ | |  \  /\  |__) \ / 
                |___ / \ \__/  |  | \__, .   |___ |___ \__> |___ | \| |__/ /~~\ |  \  |  
                                                                         
                1 IN 1,000,000 (0,0001%)
                \n\n\n\n''': 10,
                ####################
                '''\n\n\n\n

                ██████╗  █████╗ ██████╗ ██╗ █████╗ ███╗   ██╗████████╗
                ██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║╚══██╔══╝
                ██████╔╝███████║██║  ██║██║███████║██╔██╗ ██║   ██║   
                ██╔══██╗██╔══██║██║  ██║██║██╔══██║██║╚██╗██║   ██║   
                ██║  ██║██║  ██║██████╔╝██║██║  ██║██║ ╚████║   ██║   
                ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                            
                1 IN 2,000,000 (0,00005%)
                \n\n\n\n''': 5,
                ####################
                '''\n\n\n\n
                _____   _     _  ______  _____  _______ _______ _______ _____ _______        
                |       |_____| |_____/ |     | |  |  | |_____|    |      |   |       .      
                |_____  |     | |    \_ |_____| |  |  | |     |    |    __|__ |_____  .
                _______ _     _  _____  _______ _____ _______ 
                |______  \___/  |     |    |      |   |      
                |______ _/   \_ |_____|    |    __|__ |_____                                                           
                                                                                                            
                1 IN 2,000,000 (0,00005%)
                \n\n\n\n''': 5,
                ####################
                '''\n\n\n\n

                ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄  ▄▄▄▄    ▄▄▄     ▄▄▄█████▓ ██░ ██ 
                ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓█████▄ ▒████▄   ▓  ██▒ ▓▒▓██░ ██▒
                ▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░
                ▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ 
                ░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ ░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓
                ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒
                ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ▒░▒   ░   ▒   ▒▒ ░   ░     ▒ ░▒░ ░
                ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░  ░    ░   ░   ▒    ░       ░  ░░ ░
                ░          ░  ░    ░ ░      ░ ░     ░     ░            ░  ░         ░  ░  ░
                    ░                            ░            ░                                                                                     
                                                                                                                            
                1 IN 2,500,000 (0,00004%)
                \n\n\n\n''': 4,
                ####################
                '''\n\n\n\n

                      .o.       ooooooooo.     .oooooo.   ooooo   ooooo       .o.       ooooo      ooo   .oooooo.    oooooooooooo ooooo        
                     .888.      `888   `Y88.  d8P'  `Y8b  `888'   `888'      .888.      `888b.     `8'  d8P'  `Y8b   `888'     `8 `888'        
                    .8"888.      888   .d88' 888           888     888      .8"888.      8 `88b.    8  888            888          888         
                   .8' `888.     888ooo88P'  888           888ooooo888     .8' `888.     8   `88b.  8  888            888oooo8     888         
                  .88ooo8888.    888`88b.    888           888     888    .88ooo8888.    8     `88b.8  888     ooooo  888    "     888         
                 .8'     `888.   888  `88b.  `88b    ooo   888     888   .8'     `888.   8       `888  `88.    .88'   888       o  888       o 
                o88o     o8888o o888o  o888o  `Y8bood8P'  o888o   o888o o88o     o8888o o8o        `8   `Y8bood8P'   o888ooooood8 o888ooooood8 
                                                                                                                                                                               
                1 IN 3,333,333 (0,00003%)
                \n\n\n\n''': 3,
                ####################
                '''\n\n\n\n

                 ,ggg,         gg ,ggg, ,ggggggg,  ,ggggggggggg,      ,ggggggg,           ,ggg,         ,gggg,  
                dP""Y8a        88dP""Y8,8P"""""Y8bdP"""88""""""Y8,  ,dP""""""Y8b         dP""8I        d8" "8I  
                Yb, `88        88Yb, `8dP'     `88Yb,  88      `8b  d8'    a  Y8        dP   88        88  ,dP  
                 `"  88        88 `"  88'       88 `"  88      ,8P  88     "Y8P'       dP    88     8888888P"   
                     88        88     88        88     88aaaad8P"   `8baaaa           ,8'    88        88       
                     88        88     88        88     88""""Yb,   ,d8P""""           d88888888        88       
                     88        88     88        88     88     "8b  d8"          __   ,8"     88   ,aa,_88       
                     88        88     88        88     88      `8i Y8,         dP"  ,8P      Y8  dP" "88P       
                     Y8b,____,d88,    88        Y8,    88       Yb,`Yba,,_____,Yb,_,dP       `8b,Yb,_,d88b,,_   
                      "Y888888P"Y8    88        `Y8    88        Y8  `"Y8888888 "Y8P"         `Y8 "Y8P"  "Y88888                                                                                                                                       
                                                                                                            
                1 IN 5,000,000 (0,00002%)
                \n\n\n\n''': 2,
                ####################
                '''\n\n\n\n
                                                                                                                                                            
                                                                                                                                            
                `7MMF'     A     `7MF' .g8""8q. `7MM"""Mq.  `7MMF'      `7MM"""Yb.         .g8"""bgd `7MMF'  `7MMF'      db      `7MMM.     ,MMF'`7MM"""Mq. 
                  `MA     ,MA     ,V .dP'    `YM. MM   `MM.   MM          MM    `Yb.     .dP'     `M   MM      MM       ;MM:       MMMb    dPMM    MM   `MM.
                   VM:   ,VVM:   ,V  dM'      `MM MM   ,M9    MM          MM     `Mb     dM'       `   MM      MM      ,V^MM.      M YM   ,M MM    MM   ,M9 
                    MM.  M' MM.  M'  MM        MM MMmmdM9     MM          MM      MM     MM            MMmmmmmmMM     ,M  `MM      M  Mb  M' MM    MMmmdM9  
                    `MM A'  `MM A'   MM.      ,MP MM  YM.     MM      ,   MM     ,MP     MM.           MM      MM     AbmmmqMA     M  YM.P'  MM    MM       
                     :MM;    :MM;    `Mb.    ,dP' MM   `Mb.   MM     ,M   MM    ,dP'     `Mb.     ,'   MM      MM    A'     VML    M  `YM'   MM    MM       
                      VF      VF       `"bmmd"' .JMML. .JMM..JMMmmmmMMM .JMMmmmdP'         `"bmmmd'  .JMML.  .JMML..AMA.   .AMMA..JML. `'  .JMML..JMML.     
                                                                                                                                                            
                                                                                                                                                                                            
                    ___            _     _   _   _     _   _   _        _     _   _   _   _           
               /|    |  |\ |   /| / \   / \ / \ / \   / \ / \ / \    / / \   / \ / \ / \ / \ /| O/ \  
                |   _|_ | \|    | \_/ o \_/ \_/ \_/ o \_/ \_/ \_/   |  \_/ o \_/ \_/ \_/ \_/  | /O  | 
                                      /             /                \     /                       /  


                \n\n\n\n''': 1,
                ####################
                'nothing': 0
            }, 0, [], [], 0)

    def result(resultNumber, itemsProbability):
        winningIndex = 0
        for item in itemsProbability:
            if resultNumber > item:
                winningIndex += 1
        return(winningIndex)
    
    def itemsProbabilityMaker(inputDict, outputList, probabilitySum):
        temp = 0
        for i in list(inputDict.values()):
            temp = temp + i
            outputList.append(temp)
        return outputList
    
    def itemsNameMaker(inputDict, outputList):
        for i in list(inputDict.keys()):
            outputList.append(i)
        return outputList

    SQZsRNG.itemsProbability = itemsProbabilityMaker(SQZsRNG.items, SQZsRNG.itemsProbability, SQZsRNG.probabilitySum)
    SQZsRNG.itemsName = itemsNameMaker(SQZsRNG.items, SQZsRNG.itemsName)
    SQZsRNG.probabilitySum = SQZsRNG.itemsProbability[-1]

    ##########

    command = ''
    while command != 'quit':
        keyboard.read_key()
        if keyboard.is_pressed("space"):
            SQZsRNG.rollsCounter += 1
            # RNG TIME

            resultNumber = random.randint(1, SQZsRNG.probabilitySum)

            if resultNumber >= 9950000 and resultNumber < 9993000 and autostop <= 1:
                print('...')
                time.sleep(2)
            elif resultNumber >= 9993000 and resultNumber < 9999700 and autostop <= 2:
                print('...?')
                time.sleep(3)
                print('!!!')
                time.sleep(1)
            elif resultNumber >= 9999700 and resultNumber < 9999960 and autostop <= 3:
                print('...?!')
                time.sleep(3)
                print('!!!')
                time.sleep(2)
                print('&$#!#%@')
                time.sleep(1)
            elif resultNumber >= 9999960 and autostop <= 4:
                print('.........')
                time.sleep(4)
                print('...?')
                time.sleep(3)
                print('!!!!!')
                time.sleep(2)
                print('BE BLESSED BY SAQREEZ!')
                time.sleep(1)

            resultNumber = result(resultNumber, SQZsRNG.itemsProbability)

            
            print('---')
            print(SQZsRNG.itemsName[resultNumber])

        elif keyboard.is_pressed('c'):
            print('\nYou have rolled', SQZsRNG.rollsCounter, 'times in this session.\n')

        elif keyboard.is_pressed('1'):
            autostop = 1
            print('\nAutostop will now stop at 1,000 or more.\n')
        elif keyboard.is_pressed('2'):
            autostop = 2
            print('\nAutostop will now stop at 10,000 or more.\n')
        elif keyboard.is_pressed('3'):
            autostop = 3
            print('\nAutostop will now stop at 100,000 or more.\n')
        elif keyboard.is_pressed('4'):
            autostop = 4
            print('\nAutostop will now stop at 1,000,000 or more.\n')
        elif keyboard.is_pressed('5'):
            autostop = 5
            print('\nAutostop will not bother you.\n')