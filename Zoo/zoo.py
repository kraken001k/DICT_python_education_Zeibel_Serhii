print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")
#stage 1

rabbit = r"""
Switching on the camera in the rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y 
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It looks fine!"""
#rabbit
camel = r"""
Switching on the camera in the camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
look at that!"""
#camel
lion = r"""
Switching on the camera in the lion habitat...
                                                   ,w.
                                                 ,YWMMw  ,M  ,
                            _.---.._   __..---._.'MMMMMw,wMWmW,
                        _.-""        '''          YP"WMMMMMMMMMb,
                    .-' __.'                   .'     MMMMW^WMMMM;
        _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
     ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
    ,MM:.     .'.-'  .'     ;     '\    ;     ',     MMMMMMMW '"=./'-,
    WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / '=_}
    "^MP__.-'    ,-' _.--""   '_,   ;       \  ; ;MMMMMMMMMMW^''; __|
               /   .'            ; ;         )  )'{  \  '"^W^',  \  :
              /  .'             /  (        .' /     Ww._      '. '"
             /  Y,              ',  '-,=,_{   ;      MMMP'""-,   '-._.-,
            (--, )                ',_ / ') \/"")      ^"      '-,  -;"\:
The lion is roaring!"""
#lion
goose = r"""
Switching on the camera in the goose habitat...
                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
Beautiful!"""
#goose
bat = r"""
Switching on the camera in the bat habitat...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It`s doing fine."""
#bat
deer = r"""
The deer habitat...
   /|       |\
'__\\       //__'
   ||      ||
 \__'\     |'__/
   '_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;'_,   '---___________-----.-.
     ;;;                          \_\
     ';;;                          |
      ;    |                       ;
       \   \     \         |      /
        \_, \    /         \     |\
          |';|  |,,,,,,,,,/ \    \ \_
          |  |  |            \   /   |
          \  \  |            |  / \  |
           | || |            | |   | |
           | || |            | |   | |
           | || |            | |   | |
           |_||_|            |_|   |_|
           /_//_/            /_/   /_/
Pretty good!"""

animals = [rabbit, camel, lion, goose, bat, deer]

habitat = input("Please enter the number of the habitat you would like to view: >")

print(animals[int(habitat)])
print("You`ve reached the end of the program")
#stage 3

while True:
    habitat = input("Please enter the number of the habitat you would like to view: >")

    if habitat == "exit":
        print("See you later!")
        break
    if habitat.isdigit() and 0 <= int(habitat) < len(animals):
        print(animals[int(habitat)])
    else:
        print("Invalid input! Please enter a valid number, or type 'exit' to quit.")
#stage 4