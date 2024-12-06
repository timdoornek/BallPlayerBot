import ballplayerbotbuilder
import image_generator
from post_to_bsky import post_to_bsky

def main():
    #build the headshot image
    headshot_path = image_generator.build_player_image()
    #build the player text
    post_text = ballplayerbotbuilder.build_full_player()
    #post to bsky
    post = post_to_bsky(post_text, headshot_path)
    
    #print(post_text)
    #print(post.uri)

if __name__=="__main__":
    main()