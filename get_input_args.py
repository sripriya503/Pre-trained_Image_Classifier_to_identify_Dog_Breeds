import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
def get_input_args():
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type=str, default = 'pet_images', help='path to image folder')
    parser.add_argument('--arch', type=str, default = 'vgg', help='CNN Model Architecture')
    parser.add_argument('--dogfile', type=str, default = 'dognames.txt', help='text file with dog names')
    
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 
    return parser.parse_args()
