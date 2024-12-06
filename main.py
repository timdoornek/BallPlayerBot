import ballplayerbotbuilder
import image_generator
from application_constants import OUTPUT_HEADSHOT_STATIC_PATH
from post_to_bsky import post_to_bsky

def main():
    #build the headshot image
    image_generator.build_player_image()

    #build the player text
    post_text = ballplayerbotbuilder.build_full_player()

    #post to bsky
    post = post_to_bsky(post_text, OUTPUT_HEADSHOT_STATIC_PATH)
    
    print(post_text)
    print(post.uri)

if __name__=="__main__":
    main()