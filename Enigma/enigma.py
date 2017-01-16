#! python3
# Credit to reddit user /u/tangerinelion for their advice 
import re
import database


class enigma:
    """
    A simulated enigma machine that can encode and decode text
    """
    def __init__(self):
        """
        Ensures the Enigma machine has all settings
        configured for operation
        """ 
        print('Default Configuration:\n'
              '\tModel: M3\n\tRotors (left-right): I, II, III\n'
              '\tReflector: B\n\tRing Setting: AAA\n\tGround Setting: AAZ\n'
              '\tPlugboard: None')
        setting = input('Customise configuration? (Y/N): ').lower()
        if setting.startswith('y'):
            self.ground_settings()
            self.rotor_settings()
            self.plugboard_settings()
        else:
            self.rotor_settings(True)
            self.ground_settings(True)
            self.plugboard_settings(True)

    def ring_settings(self, notched_rotor, ring_offset):
        """
        The ring setting offsets the rotor key-value pairs relative
        to the value. e.g. for Rotor M3-I:
        v: ABCDEFGHIJKLMNOPQRSTUVWXYZ,  ABCDEFGHIJKLMNOPQRSTUVWXYZ
        k: UWYGADFPVZBECKMTHXSLRINQOJ,  JUWYGADFPVZBECKMTHXSLRINQO
        """
        new_keys = []
        ring_offset = database.ab_list.index(ring_offset)
        rotor = self.kv_swap(notched_rotor)
        for lttr_no in range(len(database.ab_list)):
            new_pos = lttr_no - ring_offset
            if new_pos > 25 or new_pos < 0:
                new_pos %= 26
            new_keys += rotor[database.ab_list[new_pos]]
        rotor = dict(zip(new_keys, database.ab_list))
        rotor.setdefault('notch', notched_rotor['notch'])
        rf_rotor = dict(zip(database.ab_list, new_keys))
        return rotor, rf_rotor

    def ground_settings(self, defaults=False):
        """
        Sets the ground setting (or starting position)
        of the rotors e.g. AAZ, BFX
        """
        # lmr = Left, Middle, Right
        if defaults:
            self.lmr = [0, 0, 25]
        else:
            print('Input start positions (ground setting):')
            left = database.ab_list.index(input('Left: ').upper())
            middle = database.ab_list.index(input('Middle: ').upper())
            right = database.ab_list.index(input('Right: ').upper())
            self.lmr = [left, middle, right]
        return self.lmr

    def rotor_settings(self, defaults=False):
        """
        User selection of model, rotors and reflector
        """
        rotor_db = database.database
        models = list(rotor_db.keys())

        if defaults:
            # self.rotors = rotor_db['M3']['I'],
            # self.rotors += self.kv_swap(rotor_db['M3']['I']),
            # self.rotors += rotor_db['M3']['II'],
            # self.rotors += self.kv_swap(rotor_db['M3']['II']),
            # self.rotors += rotor_db['M3']['III'],
            # self.rotors += self.kv_swap(rotor_db['M3']['III']),
            # self.rotors += rotor_db['M3']['reflectors']['B'],

            self.rotors = (rotor_db['M3']['I'], self.kv_swap(rotor_db['M3']['I'])),
            self.rotors += (rotor_db['M3']['II'], self.kv_swap(rotor_db['M3']['II'])),
            self.rotors += (rotor_db['M3']['III'], self.kv_swap(rotor_db['M3']['III'])),
            self.rotors += rotor_db['M3']['reflectors']['B'],

        else:
            print('Select model: %s' % ', '.join(models))
            model = input().title()
            rotors = rotor_db[model]
            reflectors = rotors['reflectors']

            print('Input rotor selection: '
                  '%s' % ', '.join(sorted(rotors.keys())))
            l_rotor = rotors[input('Left: ').upper()]
            m_rotor = rotors[input('Middle: ').upper()]
            r_rotor = rotors[input('Right: ').upper()]

            print('Input ring settings (A-Z):')
            l_pair = self.ring_settings(l_rotor, input('Left: ').upper())
            m_pair = self.ring_settings(m_rotor, input('Middle: ').upper())
            r_pair = self.ring_settings(r_rotor, input('Right: ').upper())

            print('Select a reflector: %s' % ', '.join(reflectors))
            reflector = reflectors[input('Reflector: ').upper()]

            # Generate reverse wiring path
            # rf_l_rotor = self.kv_swap(l_rotor)
            # rf_m_rotor = self.kv_swap(m_rotor)
            # rf_r_rotor = self.kv_swap(r_rotor)

            # self.rotors = l_rotor, m_rotor, r_rotor, reflector
            # self.rotors += rf_l_rotor, rf_m_rotor, rf_r_rotor

            self.rotors = l_pair, m_pair, r_pair, reflector

        return self.rotors

    def plugboard_settings(self, defaults=False):
        """
        Sets which letters are swapped on the plugboard
        """
        # Generate default plugboard where A='A', B='B', etc.
        plugboard = {ltr: ltr for ltr in database.ab_list}

        if defaults:
            self.plugboard = plugboard
            return self.plugboard

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
                        ltr = input('Enter a new letter (pair %s: '
                                    % count).upper()
                    while ltr in used_ltrs:
                        print('Letter already in use.')
                        ltr = input('Enter a new letter (pair %s): '
                                    % count).upper()
                    if ltr or i == 0:
                        break   # second input can't be blank
                if ltr == '':
                    break
                used_ltrs += ltr
                pair += ltr
                if i == 1:  # ensures both inputs were made
                    plugboard[pair[0]] = pair[1]
                    plugboard[pair[1]] = pair[0]
            if not pair:
                break
        self.plugboard = plugboard
        return self.plugboard

    def kv_swap(self, notched_rotor):
        """
        Swaps the key-value pairs in the rotor dictionary
        for use in the reverse path
        """
        rotor = notched_rotor.copy()
        rotor.pop('notch')
        rf_rotor = {}
        for k, v in rotor.items():
                rf_rotor.setdefault(v, k)
        return rf_rotor

    def rotor_io(self, ch, pos, rotor):
        """
        Determines the output of a letter run through a rotor
        """
        rotor_mapping = database.ab_list.index(ch) + pos
        if rotor_mapping < 0 or rotor_mapping > 25:
            rotor_mapping %= 26
        rotor_io_out = rotor[database.ab_list[rotor_mapping]]
        return rotor_io_out

    def plugboard_encode(self, keypress):
        """Runs character through the plugboard"""
        self.plugboard_out = self.plugboard.get(keypress, keypress)
        return self.plugboard_out

    def rotor_encode(self, keypress):
        """
        Runs text through the Enigma rotor mechanism
        """
        l_rotor, rf_l_rotor = self.rotors[0][0], self.rotors[0][1]
        m_rotor, rf_m_rotor = self.rotors[1][0], self.rotors[1][1]
        r_rotor, rf_r_rotor = self.rotors[2][0], self.rotors[2][1]
        reflector = self.rotors[3]

        # Start position, lmr = left, middle, right
        left, middle, right = self.lmr[0], self.lmr[1], self.lmr[2]

        print(database.ab_list[left], database.ab_list[middle],
              database.ab_list[right])

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

        self.lmr = [left, middle, right]

        # Encode character
        # Subtraction accounts for the previous rotor's rotation
        # relative to the rotor being used.
        r_rotor_out = self.rotor_io(keypress, right, r_rotor)

        m_rotor_out = self.rotor_io(r_rotor_out, middle - right, m_rotor)

        l_rotor_out = self.rotor_io(m_rotor_out, left - middle, l_rotor)

        reflector_out = self.rotor_io(l_rotor_out, -left, reflector)

        l_rotor_out = self.rotor_io(reflector_out, left, rf_l_rotor)

        m_rotor_out = self.rotor_io(
            l_rotor_out, middle - left, rf_m_rotor)

        r_rotor_out = self.rotor_io(
            m_rotor_out, right - middle, rf_r_rotor)

        rotor_encode_out = database.ab_list[database.ab_list.index(r_rotor_out) - right]
        self.rotor_encode_out = rotor_encode_out
        return self.rotor_encode_out

    def ch_input(self):
        """
        Returns only valid input characters
        Valid inputs are non-accented upper-case characters A-Z
        """
        rm_invalid_ch = re.compile(r'[A-Z]')
        keypress = ''
        while not keypress:
            keypress = input('Enter message: ').upper()
            keypress = rm_invalid_ch.findall(keypress)
        return keypress

    def encode(self):
        """
        Runs text through the Enigma machine,
        then outputs text in groups of four characters
        """
        message = self.ch_input()
        ch_list = ''
        for ch in message:
            self.plugboard_encode(ch)
            self.rotor_encode(self.plugboard_out)
            self.plugboard_encode(self.rotor_encode_out)
            ch_list += self.rotor_encode_out
        output = re.compile(r'[A-Z]{1,4}').findall(ch_list)
        output = ' '.join(output)
        return output


if __name__ == "__main__":
    machine = enigma()
    x = machine.ring_settings(machine.rotors[0][0], 'B')
    print(sorted(x[0].items()))
    print(sorted(x[1].items()))
