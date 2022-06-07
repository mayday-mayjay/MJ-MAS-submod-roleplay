#placeholder
m “...Oh! You want to roleplay with me [player]?””
m “I’m so glad you decided to try out the story idea I mentioned earlier.”
m “I’m sure it’ll be very eye-opening..”
m “By the way [player], this story will take ____ to ____ minutes.”
m “Do you have the time to actually listen to me?”
$_history_list.pop()
menu:
   “Yes.”
     m “Alright then, [player].
     m “This is the story of a prince/princess and a knight.”
     m “Does it seem familiar? Well something tells me that it will be quite the experience.”
     m “So let’s get to it…”

     –Start story–

   “No”
     m “Oh…”
     m “Well I guess I should have expected this player.”
     m “Maybe some other time then…”
     
return
