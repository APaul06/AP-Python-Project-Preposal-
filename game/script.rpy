
# Empty Variable
default protein_sequence = ""

label start:

    scene bg room #Default Background 
    
    # Intro
    menu:
        "Do You Have A Protein You Need to Find the Weight of?":
            jump calculator
            # Goes to calculator 
        "Quit":
            return #exits

#calculate molecular weight THAT IS NOT WORKING PROPERLY FOR SOME REASON Attempt 2
    init python:
        def calculate_molecular_weight(protein_sequence):
            # Molecular weights of amino acids (in Daltons)
             
            #A - Alanine, C - Cysteine, D - Aspartic Acid, E - Glutamic Acid, F - Phenylalanine, G - Glycine, H - Histidine, I - Isoleucine, K - Lysine, L - Leucine, M - Methionine, N - Asparagine, P - Proline, Q - Glutamine, R - Arginine, S - Serine, T - Threonine, V - Valine, W - Tryptophan, Y - Tyrosine
            weights = {
                'A': 89, 'R': 174, 'N': 132, 'D': 133, 
                'C': 121, 'Q': 146, 'E': 147, 'G': 75,
                'H': 155, 'I': 131, 'L': 131, 'K': 146,
                'M': 149, 'F': 165, 'P': 115, 'S': 105,
                'T': 119, 'W': 204, 'Y': 181, 'V': 117
            }
            tally = len(protein_sequence) -1 #each bond formed between acids removes a water molecule this will count the water molecules that will be removed
            molecular_weight = 0
            for _ in protein_sequence:
                if _ in weights:
                    molecular_weight += weights[_]
            molecular_weight = molecular_weight - (tally*18) #Each water molecule lost will remove 18 daltons of weight

            return molecular_weight

label calculator:
    
    # Asking for user input
    call screen protein_input
    $ molecular_weight = calculate_molecular_weight(protein_sequence)
    jump result

# Screen for user input
screen protein_input:
    vbox:
        align (0.5, 0.4)
        text "{color=#000000}Enter your protein sequence:{/color}"
        text "{color=#000000}E.g. MKCKWNRVFNIPEYRRHTDF{/color}"
        
        # Input to a Ren'Py variable

        input value VariableInputValue("protein_sequence") allow "ACDEFGHIKLMNPQRSTVWY" length 100

        
        textbutton "Calculate" action Return()
        
# After calculation
label result:
    
    # Display the result
    "The molecular weight of the protein is [molecular_weight] Daltons."

    "Image Credits: Designed by Freepik" #Credits for many of the images used

    #calculate again or quit
    menu:
        "Calculate another sequence":
            jump calculator
        "Quit":
            return
