# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):    
    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(), 
          "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    """          
    print("{:20}: {:3d}".format('% Correct Dogs', results_stats_dic['pct_correct_dogs']))
    print("{:20}: {:3d}".format('% Correct Breed', results_stats_dic['pct_correct_breed']))
    print("{:20}: {:3d}".format('% Correct "Not-a" Dog', results_stats_dic['pct_correct_notdogs']))
    """
    print(" ")
    for key in results_stats_dic:
        if key.startswith('p'):
            print("{}: {}".format(key, results_stats_dic[key]))
            
    # IF print_incorrect_dogs == True AND there were images incorrectly 
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] ) 
       ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        
        # process through results dict, printing incorrectly classified dogs
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],
                                                          results_dic[key][1]))
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
 