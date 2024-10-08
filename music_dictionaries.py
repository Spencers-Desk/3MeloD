melody_dictionary: dict[str, int] = {
    # 'ref': x_A4_feedrate,  # A4 ~ 440Hz
    'E2': -29,
    'e2': -29,
    'F2': -28,
    'f2': -28,
    'Fs2': -27,
    'fs2': -27,
    'Gf2': -27,
    'gf2': -27,
    'G2': -26,
    'g2': -26,
    'Gs2': -25,
    'gs2': -25,
    'Af2': -25,
    'af2': -25,
    'A2': -24,
    'a2': -24,
    'As2': -23,
    'as2': -23,
    'Bf2': -23,
    'bf2': -23,
    'B2': -22,
    'b2': -22,
    'C3': -21,
    'c3': -21,
    'Cs3': -20,
    'cs3': -20,
    'Df3': -20,
    'df3': -20,
    'D3': -19,
    'd3': -19,
    'Ds3': -18,
    'ds3': -18,
    'Ef3': -18,
    'ef3': -18,
    'E3': -17,
    'e3': -17,
    'F3': -16,
    'f3': -16,
    'Fs3': -15,
    'fs3': -15,
    'Gf3': -15,
    'gf3': -15,
    'G3': -14,
    'g3': -14,
    'Gs3': -13,
    'gs3': -13,
    'Af3': -13,
    'af3': -13,
    'A3': -12,
    'a3': -12,
    'As3': -11,
    'as3': -11,
    'Bf3': -11,
    'bf3': -11,
    'B3': -10,
    'b3': -10,
    'C4': -9,
    'c4': -9,
    'Cs4': -8,
    'cs4': -8,
    'Df4': -8,
    'df4': -8,
    'D4': -7,
    'd4': -7,
    'Ds4': -6,
    'ds4': -6,
    'Ef4': -6,
    'ef4': -6,
    'E4': -5,
    'e4': -5,
    'F4': -4,
    'f4': -4,
    'Fs4': -3,
    'fs4': -3,
    'Gf4': -3,
    'gf4': -3,
    'G4': -2,
    'g4': -2,
    'Gs4': -1,
    'gs4': -1,
    'Af4': -1,
    'af4': -1,
    'A4': 0,
    'a4': 0,
    'As4': 1,
    'as4': 1,
    'Bf4': 1,
    'bf4': 1,
    'B4': 2,
    'b4': 2,
    'C5': 3,
    'c5': 3,
    'Cs5': 4,
    'cs5': 4,
    'Df5': 4,
    'df5': 4,
    'D5': 5,
    'd5': 5,
    'Ds5': 6,
    'ds5': 6,
    'Ef5': 6,
    'ef5': 6,
    'E5': 7,
    'e5': 7,
    'F5': 8,
    'f5': 8,
    'Fs5': 9,
    'fs5': 9,
    'Gf5': 9,
    'gf5': 9,
    'G5': 10,
    'g5': 10,
    'Gs5': 11,
    'gs5': 11,
    'Af5': 11,
    'af5': 11,
    'A5': 12,
    'a5': 12,
    'As5': 13,
    'as5': 13,
    'Bf5': 13,
    'bf5': 13,
    'B5': 14,
    'b5': 14,
    'C6': 15,
    'c6': 15,
    'Cs6': 16,
    'cs6': 16,
    'Df6': 16,
    'df6': 16,
    'D6': 17,
    'd6': 17,
    'Ds6': 18,
    'ds6': 18,
    'Ef6': 18,
    'ef6': 18,
    'E6': 19,
    'e6': 19,
    'F6': 20,
    'f6': 20,
    'Fs6': 21,
    'fs6': 21,
    'Gf6': 21,
    'gf6': 21,
    'G6': 22,
    'g6': 22,
    'Gs6': 23,
    'gs6': 23,
    'Af6': 23,
    'af6': 23,
    'A6': 24,
    'a6': 24
}

mid_dictionary: dict[str, int] = {
    # 'ref': y_A4_feedrate,  # 4225  # issue
    'E2': -29,
    'e2': -29,
    'F2': -28,
    'f2': -28,
    'Fs2': -27,
    'fs2': -27,
    'Gf2': -27,
    'gf2': -27,
    'G2': -26,
    'g2': -26,
    'Gs2': -25,
    'gs2': -25,
    'Af2': -25,
    'af2': -25,
    'A2': -24,
    'a2': -24,
    'As2': -23,
    'as2': -23,
    'Bf2': -23,
    'bf2': -23,
    'B2': -22,
    'b2': -22,
    'C3': -21,
    'c3': -21,
    'Cs3': -20,
    'cs3': -20,
    'Df3': -20,
    'df3': -20,
    'D3': -19,
    'd3': -19,
    'Ds3': -18,
    'ds3': -18,
    'Ef3': -18,
    'ef3': -18,
    'E3': -17,
    'e3': -17,
    'F3': -16,
    'f3': -16,
    'Fs3': -15,
    'fs3': -15,
    'Gf3': -15,
    'gf3': -15,
    'G3': -14,
    'g3': -14,
    'Gs3': -13,
    'gs3': -13,
    'Af3': -13,
    'af3': -13,
    'A3': -12,
    'a3': -12,
    'As3': -11,
    'as3': -11,
    'Bf3': -11,
    'bf3': -11,
    'B3': -10,
    'b3': -10,
    'C4': -9,
    'c4': -9,
    'Cs4': -8,
    'cs4': -8,
    'Df4': -8,
    'df4': -8,
    'D4': -7,
    'd4': -7,
    'Ds4': -6,
    'ds4': -6,
    'Ef4': -6,
    'ef4': -6,
    'E4': -5,
    'e4': -5,
    'F4': -4,
    'f4': -4,
    'Fs4': -3,
    'fs4': -3,
    'Gf4': -3,
    'gf4': -3,
    'G4': -2,
    'g4': -2,
    'Gs4': -1,
    'gs4': -1,
    'Af4': -1,
    'af4': -1,
    'A4': 0,
    'a4': 0,
    'As4': 1,
    'as4': 1,
    'Bf4': 1,
    'bf4': 1,
    'B4': 2,
    'b4': 2,
    'C5': 3,
    'c5': 3,
    'Cs5': 4,
    'cs5': 4,
    'Df5': 4,
    'df5': 4,
    'D5': 5,
    'd5': 5,
    'Ds5': 6,
    'ds5': 6,
    'Ef5': 6,
    'ef5': 6,
    'E5': 7,
    'e5': 7,
    'F5': 8,
    'f5': 8,
    'Fs5': 9,
    'fs5': 9,
    'Gf5': 9,
    'gf5': 9,
    'G5': 10,
    'g5': 10,
    'Gs5': 11,
    'gs5': 11,
    'Af5': 11,
    'af5': 11,
    'A5': 12,
    'a5': 12,
    'As5': 13,
    'as5': 13,
    'Bf5': 13,
    'bf5': 13,
    'B5': 14,
    'b5': 14,
    'C6': 15,
    'c6': 15,
    'Cs6': 16,
    'cs6': 16,
    'Df6': 16,
    'df6': 16,
    'D6': 17,
    'd6': 17,
    'Ds6': 18,
    'ds6': 18,
    'Ef6': 18,
    'ef6': 18,
    'E6': 19,
    'e6': 19,
    'F6': 20,
    'f6': 20,
    'Fs6': 21,
    'fs6': 21,
    'Gf6': 21,
    'gf6': 21,
    'G6': 22,
    'g6': 22,
    'Gs6': 23,
    'gs6': 23,
    'Af6': 23,
    'af6': 23,
    'A6': 24,
    'a6': 24
}

bass_dictionary: dict[str, int] = {
    # 'ref': z_A4_feedrate,
    'E1': -41,
    'e1': -41,
    'F1': -40,
    'f1': -40,
    'Fs1': -39,
    'fs1': -39,
    'Gf1': -39,
    'gf1': -39,
    'G1': -38,
    'g1': -38,
    'Gs1': -37,
    'gs1': -37,
    'Af1': -37,
    'af1': -37,
    'A1': -36,
    'a1': -36,
    'As1': -35,
    'as1': -35,
    'Bf1': -35,
    'bf1': -35,
    'B1': -34,
    'b1': -34,
    'C2': -33,
    'c2': -33,
    'Cs2': -32,
    'cs2': -32,
    'Df2': -32,
    'df2': -32,
    'D2': -31,
    'd2': -31,
    'Ds2': -30,
    'ds2': -30,
    'Ef2': -30,
    'ef2': -30,
    'E2': -29,
    'e2': -29,
    'F2': -28,
    'f2': -28,
    'Fs2': -27,
    'fs2': -27,
    'Gf2': -27,
    'gf2': -27,
    'G2': -26,
    'g2': -26,
    'Gs2': -25,
    'gs2': -25,
    'Af2': -25,
    'af2': -25,
    'A2': -24,
    'a2': -24,
    'As2': -23,
    'as2': -23,
    'Bf2': -23,
    'bf2': -23,
    'B2': -22,
    'b2': -22,
    'C3': -21,
    'c3': -21,
    'Cs3': -20,
    'cs3': -20,
    'Df3': -20,
    'df3': -20,
    'D3': -19,
    'd3': -19,
    'Ds3': -18,
    'ds3': -18,
    'Ef3': -18,
    'ef3': -18,
    'E3': -17,
    'e3': -17,
    'F3': -16,
    'f3': -16,
    'Fs3': -15,
    'fs3': -15,
    'Gf3': -15,
    'gf3': -15,
    'G3': -14,
    'g3': -14,
    'Gs3': -13,
    'gs3': -13,
    'Af3': -13,
    'af3': -13,
    'A3': -12,
    'a3': -12,
    'As3': -11,
    'as3': -11,
    'Bf3': -11,
    'bf3': -11,
    'B3': -10,
    'b3': -10,
    'C4': -9,
    'c4': -9,
    'Cs4': -8,
    'cs4': -8,
    'Df4': -8,
    'df4': -8,
    'D4': -7,
    'd4': -7,
    'Ds4': -6,
    'ds4': -6,
    'Ef4': -6,
    'ef4': -6,
    'E4': -5,
    'e4': -5,
    'F4': -4,
    'f4': -4,
    'Fs4': -3,
    'fs4': -3,
    'Gf4': -3,
    'gf4': -3,
    'G4': -2,
    'g4': -2,
    'Gs4': -1,
    'gs4': -1,
    'Af4': -1,
    'af4': -1,
    'A4': 0,
    'a4': 0,
    'As4': 1,
    'as4': 1,
    'Bf4': 1,
    'bf4': 1,
    'B4': 2,
    'b4': 2,
    'C5': 3,
    'c5': 3,
    'Cs5': 4,
    'cs5': 4,
    'Df5': 4,
    'df5': 4,
    'D5': 5,
    'd5': 5,
    'Ds5': 6,
    'ds5': 6,
    'Ef5': 6,
    'ef5': 6,
    'E5': 7,
    'e5': 7,
    'F5': 8,
    'f5': 8,
    'Fs5': 9,
    'fs5': 9,
    'Gf5': 9,
    'gf5': 9,
    'G5': 10,
    'g5': 10,
    'Gs5': 11,
    'gs5': 11,
    'Af5': 11,
    'af5': 11,
    'A5': 12,
    'a5': 12,
    'As5': 13,
    'as5': 13,
    'Bf5': 13,
    'bf5': 13,
    'B5': 14,
    'b5': 14,
    'C6': 15,
    'c6': 15,
    'Cs6': 16,
    'cs6': 16,
    'Df6': 16,
    'df6': 16,
    'D6': 17,
    'd6': 17,
    'Ds6': 18,
    'ds6': 18,
    'Ef6': 18,
    'ef6': 18,
    'E6': 19,
    'e6': 19,
    'F6': 20,
    'f6': 20,
    'Fs6': 21,
    'fs6': 21,
    'Gf6': 21,
    'gf6': 21,
    'G6': 22,
    'g6': 22,
    'Gs6': 23,
    'gs6': 23,
    'Af6': 23,
    'af6': 23,
    'A6': 24,
    'a6': 24
}
