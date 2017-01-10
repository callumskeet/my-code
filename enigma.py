#! python3
# enigma.py - A simulated enigma machine that can encode and decode text
import re
from rotors import *


class enigma:

    def settings():
        '''Ensures the Enigma machine has all settings
        configured for operation'''
        print('Default Configuration:\n'
              '\tModel: M3\n\tRotors (left-right): I, II, III\n'
              '\tReflector: B\n\tGround Setting: AAZ\n\tPlugboard: None')
        setting = input('Customise configuration? (Y/N): ').lower()
        if setting.startswith('y'):
            enigma.ground_settings()
            enigma.rotor_settings()
            enigma.plugboard_settings()
            return False
        else:
            enigma.rotor_settings(True)
            enigma.ground_settings(True)
            enigma.plugboard_settings(True)
            return False

    def ground_settings(defaults=False):
        '''Sets the ground setting (or starting position)
        of the rotors e.g. AAZ, BFX'''
        if defaults:
            enigma.lmr = [0, 0, 25]
        else:
            print('Input start positions (ground setting):')
            left = ab_list.index(input('Left: ').upper())
            middle = ab_list.index(input('Middle: ').upper())
            right = ab_list.index(input('Right: ').upper())
            enigma.lmr = [left, middle, right]
        return enigma.lmr

    def rotor_settings(defaults=False):
        '''User selection of model, rotors and reflector'''
        models = ['M3', 'Swiss K']
        rotors = {'M3': {'I': I_roman, 'II': II_roman, 'III': III_roman,
                         'IV': IV_roman, 'V': V_roman},
                  'Swiss K': {'I-K': I_K, 'II-K': II_K, 'III-K': III_K}}
        reflectors = {'M3': {'B': rf_b, 'C': rf_c},
                      'Swiss K': {'UKW-K': UKW_K, 'ETW-K': ETW_K}}

        if defaults:
            enigma.rotors = I_roman, II_roman, III_roman, rf_b,
            enigma.rotors += enigma.kv_swap(I_roman),
            enigma.rotors += enigma.kv_swap(II_roman),
            enigma.rotors += enigma.kv_swap(III_roman),

        else:
            print('Select model: %s' % ', '.join(models))
            model = input().title()
            rotors = rotors[model]
            reflectors = reflectors[model]

            print('Input rotor selection: '
                  '%s' % ', '.join(sorted(rotors.keys())))
            l_rotor = rotors[input('Left: ').upper()]
            m_rotor = rotors[input('Middle: ').upper()]
            r_rotor = rotors[input('Right: ').upper()]

            print('Select a reflector: %s' % ', '.join(reflectors))
            reflector = reflectors[input('Reflector: ').upper()]

            # Generate reverse wiring path
            rf_l_rotor = enigma.kv_swap(l_rotor)
            rf_m_rotor = enigma.kv_swap(m_rotor)
            rf_r_rotor = enigma.kv_swap(r_rotor)

            enigma.rotors = l_rotor, m_rotor, r_rotor, reflector
            enigma.rotors += rf_l_rotor, rf_m_rotor, rf_r_rotor

        return enigma.rotors

    def plugboard_settings(defaults=False):
        '''Sets which letters are swapped on the plugboard'''
        # Generate default plugboard where A='A', B='B', etc.
        plugboard = {ltr: ltr for ltr in ab_list}

        if defaults:
            enigma.plugboard = plugboard
            return enigma.plugboard

        print('Input letter pairs for plugboard settings.\n'
              'Leave blank for defaults or to continue.')

        used_ltrs = []
        for count in range(1, 11):
            pair = []
            for i in range(2):
                ltr = input('Enter a letter (pair %s): ' % count).upper()
                while True:
                    while ltr == '' and i == 1:
                        print("Input can't be blank.")
                        ltr = input('Enter a new letter: ').upper()
                    while ltr in used_ltrs:
                        print('Letter already in use.')
                        ltr = input('Enter a new letter (pair %s): '
                                    % count).upper()
                    if bool(ltr):
                        break   # second input can't be blank
                    elif i == 0:
                        break   # okay if first input blank
                if ltr == '':
                    break
                used_ltrs += ltr
                pair += ltr
                if i == 1:  # ensures both inputs were made
                    plugboard[pair[0]] = pair[1]
                    plugboard[pair[1]] = pair[0]
            if pair == []:
                break
        enigma.plugboard = plugboard
        return enigma.plugboard

    def kv_swap(rotor):
        '''Swaps the key-value pairs in the rotor dictionary
        for use in the reverse path'''
        rf_rotor = {}
        for k, v in rotor.items():
            rf_rotor.setdefault(v, k)
        return rf_rotor

    def rotor_io(ch, pos, rotor):
        '''Determines the output of a letter run through a rotor'''
        rotor_mapping = ab_list.index(ch) + pos
        if rotor_mapping > 25:
            rotor_mapping -= 26
        elif rotor_mapping < 0:
            rotor_mapping += 26
        rotor_io_out = rotor[ab_list[rotor_mapping]]
        return rotor_io_out

    def plugboard_encode(keypress):
        '''Runs character through the plugboard'''
        plugboard = enigma.plugboard
        input_letter = keypress
        if input_letter in plugboard.keys():
            output_letter = plugboard[input_letter]
        else:
            output_letter = input_letter
        enigma.plugboard_out = output_letter
        return enigma.plugboard_out

    def rotor_encode(keypress):
        '''Runs text through the Enigma rotor mechanism'''
        l_rotor, m_rotor = enigma.rotors[0], enigma.rotors[1]
        r_rotor = enigma.rotors[2]
        reflector = enigma.rotors[3]
        rf_l_rotor, rf_m_rotor = enigma.rotors[4], enigma.rotors[5]
        rf_r_rotor = enigma.rotors[6]

        # Start position, lmr = left, middle, right
        left, middle, right = enigma.lmr[0], enigma.lmr[1], enigma.lmr[2]

        while True:
            print(ab_list[left], ab_list[middle], ab_list[right])

            # Increment rotor position
            right += 1
            if right > 25:
                right = 0
            elif right == r_rotor['notch']:
                middle += 1
            if middle > 25:
                middle = 0
            elif middle == (m_rotor['notch'] - 1) and right == (
                    r_rotor['notch'] + 1):
                middle += 1
                left += 1
            if left > 25:
                left = 0

            enigma.lmr[0], enigma.lmr[1], enigma.lmr[2] = left, middle, right

            # encode character
            # Subtraction compensates for the previous rotor's rotation
            # relative to the rotor being used.
            r_rotor_out = enigma.rotor_io(keypress, right, r_rotor)

            m_rotor_out = enigma.rotor_io(r_rotor_out, middle - right, m_rotor)

            l_rotor_out = enigma.rotor_io(m_rotor_out, left - middle, l_rotor)

            reflector_out = enigma.rotor_io(l_rotor_out, -left, reflector)

            l_rotor_out = enigma.rotor_io(reflector_out, left, rf_l_rotor)

            m_rotor_out = enigma.rotor_io(
                l_rotor_out, middle - left, rf_m_rotor)

            r_rotor_out = enigma.rotor_io(
                m_rotor_out, right - middle, rf_r_rotor)

            rotor_encode_out = ab_list[ab_list.index(r_rotor_out) - right]
            enigma.rotor_encode_out = rotor_encode_out
            return enigma.rotor_encode_out

    def ch_input():
        '''Returns only valid input characters'''
        rm_invalid_ch = re.compile(r'[A-Z]')
        keypress = ''
        while not bool(keypress):
            keypress = input('Enter message: ').upper()
            keypress = rm_invalid_ch.findall(keypress)
        return keypress

    def encode():
        '''Runs text through the Enigma machine'''
        keypress = enigma.ch_input()
        output = []
        for ch in keypress:
            enigma.plugboard_encode(ch)
            enigma.rotor_encode(enigma.plugboard_out)
            enigma.plugboard_encode(enigma.rotor_encode_out)
            output += enigma.rotor_encode_out
        output = ''.join(output)
        return output


if __name__ == "__main__":
    enigma.settings()
    print(enigma.encode())
