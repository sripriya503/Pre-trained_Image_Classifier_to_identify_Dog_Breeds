from classifier import classifier 

# TODO 3: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 3" for the classify_images function 
#       Specifically EDIT and ADD code to define the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
       
       # TODO: 3a. Set the string variable model_label to be the string that's 
       #           returned from using the classifier function instead of the   
       #           empty string below.
       #
       #  Runs classifier function to classify the images classifier function 
       # inputs: path + filename  and  model, returns model_label 
       # as classifier label
       model_label = ""

       # TODO: 3b. BELOW REPLACE pass with CODE to process the model_label to 
       #           convert all characters within model_label to lowercase 
       #           letters and then remove whitespace characters from the ends
       #           of model_label. Be certain the resulting processed string 
       #           is named model_label.
       #
       # Processes the results so they can be compared with pet image labels
       # set labels to lowercase (lower) and stripping off whitespace(strip)
       pass
              
       # defines truth as pet image label 
       truth = results_dic[key][0]

       # TODO: 3c. REPLACE pass BELOW with CODE that uses the extend    list function
    #           to add the classifier label (model_label) and the value of
       #           1 (where the value of 1 indicates a match between pet image 
       #           label and the classifier label) to the results_dic dictionary
       #           for the key indicated by the variable key 
       #
       # If the pet image label is found within the classifier label list of terms 
       # as an exact match to on of the terms in the list - then they are added to 
       # results_dic as an exact match(1) using extend list function
       if truth in model_label:
           pass

       # TODO: 3d. REPLACE pass BELOW with CODE that uses the extend list function
       #           to add the classifier label (model_label) and the value of
       #           0 (where the value of 0 indicates NOT a match between the pet 
       #           image label and the classifier label) to the results_dic 
       #           dictionary for the key indicated by the variable key
       #                   
       # if not found then added to results dictionary as NOT a match(0) using
       # the extend function 
       else:
           pass
