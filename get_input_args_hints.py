import argparse

# TODO 1: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 1" for the get_input_args function
#       Please be certain to replace None in the return statement with 
#       parser.parse_args() parsed argument collection that you created with 
#       this function
# 
def get_input_args():
    # Creates parse 
    parser = argparse.ArgumentParser()

    # Creates 3 command line arguments args.dir for path to images files,
    # args.arch which CNN model to use for classification, args.labels path to
    # text file with names of dogs.
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to folder of images')
    # TODO: 1a. EDIT parse.add_argument statements BELOW to add type & help for:
    #          --arch - the CNN model architecture
    #          --dogfile - text file of names of dog breeds
    parser.add_argument('--arch', default = 'vgg' )
    parser.add_argument('--dogfile', default = 'dognames.txt' )

    # TODO: 1b. Replace None with parser.parse_args() parsed argument 
    # collection that you created with this function 
    return None
