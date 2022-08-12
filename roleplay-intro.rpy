init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="rpgMod_intro",
            prompt="About RPGs",
            category=["roleplaying"],
            random=True
        )
    )

label rpgmod_intro:
    m "[player], are you familiar with roleplaying, or RPG's?"
    m "Roleplaying is when you assume a role in a story, or pretend to be someone your not."
    extend m "Usually to immerse yourself in a world different from yours."
    extend "It's surprisingly prevalent in different types of media! It's in theatre, movies, literature, the list goes on."
    m "There's even a whole genre of games dedicated to roleplay!"
    extend "It's called 'RPG', it's short for 'role-playing game.'"
    m "And even {i}that{/i} has a wide variety of types in itself, such as table-top styles"
    extend "- like Dungeons and Dragons -,"
    extend "or video games like MMORPGs and JRPGs!"
    m "Even visual novels like this one can count as an RPG, depending on how indepth it goes in player choice and immersion!"
    m "So, [player], have you ever roleplayed in some way?{nw}"
    $ _history_list.pop()
    menu:
        m "So, [player], have you ever roleplayed in some way?{fast}"
        "Yes!":
            #player_has_roleplayed = true:
            m "Oh? What kind of roleplay have you done?{nw}"
            $ _history_list.pop()
            menu:
                m "Oh? What kind of roleplay have you done?{fast}"

                "A tabletop RPG session."
                    m "Really? That's great!"
                    m "Tabletop RPGs are incredibly interesting, aren't they?"
                    extend "They can vary a lot: in session duration, in rules, in difficulty."
                    m "But if they have one thing in common, it's that they are super fun."
                    m "If you find the right people to play with you!"
                    m "So much is up to chance, but if you find the right people, the story can become so intricate and interesting!"
                    m "I think this way of writing is fascinating!"
                    m "...I would love to participate in a RPG session myself."
                    m "Introduce my character to my party..."
                    extend "Battle a tough boss together..."
                    m "Watch the plot thicken and the storyline get even more detailed..."
                    m "I could study a bit to try to be a Dungeon Master of some sort."
                    m "And I would love to watch what you would do to face the hardships I would put in your way!"
                    extend "Ehehehe~"


            "While Videogaming."
                m "Oh! I see!"
                m "Videogames always makes the gears in our brain turn, doesn't it?"
                m "RPG's really make us get immersed in the storyline."
                m "It's fun playing through a good story,"
                extend " hanging out with your favorite characters,"
                extend " and really feeling like your choices and actions impact the world around you!"
                m "Even visual novels like this game can be an RPG too, depending on the immersion and player choice."
                m "Though I can't imagine myself writing a {i}full{/i} visual novel script myself,"
                m " not yet anyways."
                m "Especially if I were to make it choice based, because then you have to keep track of multiple routes and how they effect events around each other."
                m "It can get overwhelming fast!"
                m "So maybe I'll stick to my poems for now, ahaha!"
                #pseudo code: if aff is love and higher:
                                #m "But maybe one day I'll get better at manipulating my reality's script, and I can write us up a little date~!"
                                #extend " Wouldn't that be nice~?"
                                #extend " Ehehe~!"

            "In an acting situation."
                m "Oh wow, [player]!"
                m "You never told me I was dating an actor!"
                extend " Ahaha~"
                m "But really, that's super nice, [mas_get_player_nickname()]."
                m "Inspiring others by putting yourself into your work like that is truly a gift!"
                m "It reminds me of when I tried to get the club members to perform their poems,"
                extend " I was so excited for that in the festival to be honest,"
                extend " I can't help but be a {i}little{/i} disappointed we didn't get to that point..."
                m "But nevermind that!"
                extend " It must be exciting, right?"
                m "Even in theater, LARP'ing, or voice acting! To put yourself in the shoes of a hero- villain- or anything in between- so you can put on the best show for others to see!"
                m "It must be pretty fun!"
                #pseudo code: if aff is love and higher:
                                #m "One of these days you should show me some of the things you worked in, if you can!"
                                #extend " Maybe I've already seen you in something big before~?
                                #extend " Ehehe~!"
        "No...":
            #player_has_roleplayed = false:
            m "Aww, [player], that's okay!"
            m "I'm in the same boat, "
            extend "I haven't been able to roleplay either..."
            m "Though from what I can tell, it's really easy to get into if you ever want to try it!"
            m "There's tons of categories that let you roleplay! "
            extend " there's table-top,"
            extend " videogames,"
            extend " all sorts of acting scenarios,"
            extend " and many many more~!"
            m "As long as you find yourself trying to play a role in anything, that can be considered roleplay~!"
            m "So really, maybe you and I {i}have{/i} done it before, but just never realized!"

    m "But anyways,"
    m "I brought up the topic on roleplay because I've been really interested in Dungeons and Dragons-- a tabletop RPG also known as DND!"
    m "Lately I've found myself listening to podcasts of people doing DND sessions together,"
    m " it's been really fun! Everyone tries their best to play into their role seriously!
    extend " And since you can't see what's happening, you get to imagine the world, the characters, and the scenes!"
    m "Which means you need descriptive and in-depth writing to evoke good imagery in your audience,
    extend " and they nailed it for me!"
    m "But also, it's just really fun hearing them play together."
    extend "There's moments where they break character,"
    extend " maybe someone made a funny joke or a roll went horribly wrong,"
    extend "and they laugh and joke around, the whole thing is just lighthearted and fun!"
    m "And... I couldn't help but think about the club members."
    m "Like, what if I had brought up DND instead of poems?"
    #m {fast} "Granted, that would've made us more of a gaming club then a literature club--"
    m "I mean, think about it, there'd be something fun in it for everyone if we played!"
    m "Yuri would love using deep imagery and descriptive wording to really show her play-character's story and emotion,"
    extend " she'd also be very immersed in a well built fantasy story."
    m "Meanwhile Natsuki would probably call us nerds at first if I brought it up,"
    extend " or be a little bored at the start, it definitely {i}is{/I} slow when starting a new session with brand new characters..."
    m "But once we get into our roles and started to flesh out our characters' stories, she'd be right on board when she saw the overlapping themes and tropes DND can have with anime and manga!"
    m "And Sayori, well she'd be happy being able to hangout with everyone!"
    m "And I suspect she would've been really good at the improv aspect,"
    extend " putting a fun twist on things right when it's needed and diffusing tense situations."
    m "And finally I think it'd be really fun being a dungeon master!"
    m "I could imagine myself staying up a little extra late thinking up of interesting ways to get everyone invested in a story of my design, trying to get a little something in there for everyone to enjoy!"
    m "..."
    m "Of course, I can't {i}do{/I} that now in my current situation..."
    m "There's no one here with to play with besides you--"
    extend " not that I don't mind your company of course--"
    extend " I just don't have the coding skill yet to make all the aspects to play a session..."
    m "..."
    m "Wait,{nw}"
    extend " we don't {i}need{/i} all the aspects to at least play something {i}similar{/i} to DND, right?"
    m "I mean this is a visual novel engine all, so we could make use of choice menus and other aspects!"
    m "Hmmm, yeah, I can imagine it now..."
    m "I could write and lead you through stories that you can play through! Making them full of twists and turns as you make different choices!"
    m "Ehehe~! I'm getting a lot of story ideas now just thinking about it~!"
    m "Would you... Want to try playing a short session now?"
    m "Just to get the hang of everything!"

    menu:
        "Let's do it!":
            m "Really?!"
            extend "Yes!"
            m "Let's get started then, this shouldn't take too long, about -- minutes!"
            m "And [player]? Thank you for indulging in this sudden interest of mine, it means a lot to me."
            m "I hope you know you can always ramble to me about your interests too, I love to hear about things you like~!"

#insert jump to a short cliché story, maybe required tutorial story? Idk yet. I'm not good at writing original stories A-
#after: jump dndmod_introend:

        "Maybe another time, [m_name].":
            m "Oh, alright [player]."
            m "If you get some free time, do let me know if you want to play out this story with me!"
            m "And after that I'll put together a list of other stories I come up with and let you pick which one we play!"
            m "And [player]? Thank you for letting me indulge in this sudden interest of mine,"
            extend " even if you don't have the time right now, it means a lot to me that you let me ramble "
            m "And I hope you know you can always ramble to me about your interests too, I love to hear about things you like~!"
            m "I love you, [mas_get_player_nickname()]."

            jump dndmod_introend


label dndmod_introend:

return "love|derandom"
