def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = dict()

    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in dognames from first line in file
        line = infile.readline()

        # Processes each line in file until reaching EOF (end-of-file) by 
        # processing line and adding dognames to dognames_dic with while loop
        while line != "":

            # TODO: 4a. REPLACE pass with CODE to remove the newline character
            #           from the variable line  
            #
            # Process line by striping newline from line
            pass

            # TODO: 4b. REPLACE pass with CODE to check if the dogname(line) 
            #          exists within dognames_dic, then if the dogname(line) 
            #          doesn't exist within dognames_dic then add the dogname(line) 
            #          to dognames_dic as the 'key' with the 'value' of 1. 
            #
            # adds dogname(line) to dogsnames_dic if it doesn't already exist 
            # in the dogsnames_dic dictionary
            pass 

            # Reads in next line in file to be processed with while loop
            # if this line isn't empty (EOF)
            line = infile.readline()

                
    # Add to whether pet labels & classifier labels are dogs by appending
    # two items to end of value(List) in results_dic. 
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    # How - iterate through results_dic if labels are found in dognames_dic
    # then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
    for key in results_dic:

        # Pet Image Label IS of Dog (e.g. found in dognames_dic)
        if results_dic[key][0] in dognames_dic:
            
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (1, 1) because both labels are dogs
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))

            # TODO: 4c. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (1,0) to the value using 
            #           the extend list function. This indicates
            #           the pet label is-a-dog, classifier label is-NOT-a-dog. 
            #                              
            # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic)
            # appends (1,0) because only pet label is a dog
            else:
                pass

        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else:
            # TODO: 4d. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (0,1) to the value uisng
            #           the extend list function. This indicates
            #           the pet label is-NOT-a-dog, classifier label is-a-dog. 
            #                              
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (0, 1)because only Classifier labe is a dog
            if results_dic[key][1] in dognames_dic:
                pass

            # TODO: 4e. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (0,0) to the value using the 
            #           extend list function. This indicates
            #           the pet label is-NOT-a-dog, classifier label is-NOT-a-dog. 
            #                                              
            # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic)
            # appends (0, 0) because both labels aren't dogs
            else:
                pass
    