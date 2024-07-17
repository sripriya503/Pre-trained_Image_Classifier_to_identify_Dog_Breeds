# TODO 6: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 6" for the print_results function.
#       Specifically edit and add code below within the the print_results function. 
#       Notice that this function doesn't return anything because it prints 
#       a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):   
    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(), 
          "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))

    # TODO: 6a. REPLACE print("") with CODE that prints the text string 
    #          'N Not-Dog Images' and then the number of NOT-dog images 
    #          that's accessed by key 'n_notdogs_img' using dictionary 
    #          results_stats_dic
    #
    print("")


    # Prints summary statistics (percentages) on Model Run
    print(" ")
    for key in results_stats_dic:
        # TODO: 6b. REPLACE pass with CODE that prints out all the percentages 
        #           in the results_stats_dic dictionary. Recall that all 
        #           percentages in results_stats_dic have 'keys' that start with 
        #           the letter p. You will need to write a conditional 
        #           statement that determines if the key starts with the letter
        #           'p' and then you want to use a print statement to print 
        #           both the key and the value. Remember the value is accessed 
        #           by results_stats_dic[key]
        #
        pass 


    # IF print_incorrect_dogs == True AND there were images incorrectly 
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] ) 
       ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # process through results dict, printing incorrectly classified dogs
        for key in results_dic:

            # TODO: 6c. REPLACE pass with CODE that prints out the pet label 
            #           and the classifier label from results_dic dictionary    
            #           ONLY when the classifier function (classifier label) 
            #           misclassified dogs specifically: 
            #             pet label is-a-dog and classifier label is-NOT-a-dog 
            #               -OR- 
            #             pet label is-NOT-a-dog and classifier label is-a-dog 
            #          You will need to write a conditional statement that 
            #          determines if the classifier function misclassified dogs
            #          See 'Adjusting Results Dictionary' section in 
            #         'Classifying Labels as Dogs' for details on the 
            #          format of the results_dic dictionary. Remember the value
            #          is accessed by results_dic[key] and the value is a list
            #          so results_dic[key][idx] - where idx represents the 
            #          index value of the list and can have values 0-4.
            #
            # Pet Image Label is a Dog - Classified as NOT-A-DOG -OR- 
            # Pet Image Label is NOT-a-Dog - Classified as a-DOG
            pass

    # IF print_incorrect_breed == True AND there were dogs whose breeds 
    # were incorrectly classified - print out these cases                    
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']) 
       ):
        print("\nINCORRECT Dog Breed Assignment:")

        # process through results dict, printing incorrectly classified breeds
        for key in results_dic:

            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if ( sum(results_dic[key][3:]) == 2 and
                results_dic[key][2] == 0 ):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],
                                                          results_dic[key][1]))
