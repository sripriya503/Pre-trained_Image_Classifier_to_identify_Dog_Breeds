from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    results_dic = dict()

    for idx in range(0, len(in_files), 1):
       
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
       if in_files[idx][0] != ".":

           # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
           #          filename in the in_files list to extract the dog breed 
           #          name from the filename. Recall that each filename can be
           #          accessed by in_files[idx]. Be certain to place the 
           #          extracted dog breed name in the variable pet_label 
           #          that's created as an empty string ABOVE
           low_pet_image = in_files[idx].lower()
           word_list_pet_image = low_pet_image.split("_")
           pet_name = ""
           for word in word_list_pet_image:
               if word.isalpha():
                   pet_name += word + " "
           pet_name = pet_name.strip()
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_name]
              
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])

        
     
    return results_dic