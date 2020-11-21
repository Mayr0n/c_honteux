def listemots(path):
    input_file = open(path, "r")
    name = input_file.name
    if len(name) >= 5:  # n.txt
        # name[:1]
        content = input_file.read()
        word_list = []  # liste des mots dans le fichier
        sentences_times = [[] for i in range(99999)]  # liste des listes des numéros de phrases où un mot apparait.

        #   ["Elle",           "se"]                  word_list
        # [[1, 1, 2, 3, 6],    [1,2]]                 sentences_times

        # word_list[0] => "Elle" ;  sentences_time[0] => [1, 1, 2, 3, 6]
        # word_list[1] => "se" ;  sentences_time[] => [1,2]

        sentences_list = content.split(".")

        #
        #  /!\ Caractères non-alphabéticonumériques
        #

        for i in range(len(sentences_list)):  # pour chaque phrase exécuter...
            sentence = sentences_list[i]
            # sentences_list[0] = sentence = Elle se tenait là, devant moi.
            word_in_sentence_list = sentence.split(" ")
            # word_in_sentence_list = ["Elle", "se", "tenait", "là,", "devant", "moi"]
            for word in word_in_sentence_list:
                word = word.lower()
                if word not in word_list:
                    word_list.append(word)
                position = word_list.index(word)
                print(word)
                print(position)
                print(sentences_times)
                sentences_times[position].append(i + 1)
                print(sentences_times)

        wl = sorted(word_list)
        st = []

        for word in wl:
            position = word_list.index(word)
            st.append(sentences_times[position])

        txt = ""

        # i = i + 1 <=> i += 1

        for i in range(len(wl)):  # pour chaque mot dans la liste des mots triés dans l'ordre alphabétique
            txt += "{} / {} / {} \n".format(wl[i], len(st[i]), st[i])

            # [1,1,2,4,5] => "1 1 2 4 5"
            # [1,1,2,4,5] => "[1,1,2,4,5]"

        file_output = open("motsde" + name, "w")  # fichier final (ouvert en mode écritre)
        file_output.write(txt)
        file_output.close()

        print("Terminé !")
    else:
        print("t'es nul")


listemots("tameh.txt")
