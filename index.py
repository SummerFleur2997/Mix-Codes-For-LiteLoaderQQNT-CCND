CJK = []
JP_Hiragana = []
JP_Katakana = []
Latin_Cap = []
Greek_Cap = []
Russia_Cap_name = []
Number = []

for i in range(19968, 40960):
    hex_num = str(hex(i))
    CJK.append(hex_num)

JP = ["0x3041", "0x3042", "0x3043", "0x3044", "0x3045", "0x3046", "0x3047", "0x3048", "0x3049",
      "0x304a", "0x304b", "0x304c", "0x304d", "0x304e", "0x304f", "0x3050", "0x3051", "0x3052",
      "0x3053", "0x3054", "0x3055", "0x3056", "0x3057", "0x3058", "0x3059", "0x305a", "0x305b",
      "0x305c", "0x305d", "0x305e", "0x305f", "0x3060", "0x3061", "0x3062", "0x3063", "0x3064",
      "0x3065", "0x3066", "0x3067", "0x3068", "0x3069", "0x306a", "0x306b", "0x306c", "0x306d",
      "0x306e", "0x306f", "0x3070", "0x3071", "0x3072", "0x3073", "0x3074", "0x3075", "0x3076",
      "0x3077", "0x3078", "0x3079", "0x307a", "0x307b", "0x307c", "0x307d", "0x307e", "0x307f",
      "0x3080", "0x3081", "0x3082", "0x3083", "0x3084", "0x3085", "0x3086", "0x3087", "0x3088",
      "0x3089", "0x308a", "0x308b", "0x308c", "0x308d", "0x308e", "0x308f", "0x3090", "0x3091",
      "0x3092", "0x3093", "0x3094", "0x309d", "0x309e", "0x30a1", "0x30a2", "0x30a3", "0x30a4",
      "0x30a5", "0x30a6", "0x30a7", "0x30a8", "0x30a9", "0x30aa", "0x30ab", "0x30ac", "0x30ad",
      "0x30ae", "0x30af", "0x30b0", "0x30b1", "0x30b2", "0x30b3", "0x30b4", "0x30b5", "0x30b6",
      "0x30b7", "0x30b8", "0x30b9", "0x30ba", "0x30bb", "0x30bc", "0x30bd", "0x30be", "0x30bf",
      "0x30c0", "0x30c1", "0x30c2", "0x30c3", "0x30c4", "0x30c5", "0x30c6", "0x30c7", "0x30c8",
      "0x30c9", "0x30ca", "0x30cb", "0x30cc", "0x30cd", "0x30ce", "0x30cf", "0x30d0", "0x30d1",
      "0x30d2", "0x30d3", "0x30d4", "0x30d5", "0x30d6", "0x30d7", "0x30d8", "0x30d9", "0x30da",
      "0x30db", "0x30dc", "0x30dd", "0x30de", "0x30df", "0x30e0", "0x30e1", "0x30e2", "0x30e3",
      "0x30e4", "0x30e5", "0x30e6", "0x30e7", "0x30e8", "0x30e9", "0x30ea", "0x30eb", "0x30ec",
      "0x30ed", "0x30ee", "0x30ef", "0x30f0", "0x30f1", "0x30f2", "0x30f3", "0x30f4", "0x30f5",
      "0x30f6", "0x30f7", "0x30f8", "0x30f9", "0x30fa", "0x30fc", "0x30fd", "0x30fe"]

Latin_vowel = ["a", "A", "i", "I", "u", "U", "e", "E", "o", "O"]
Katakana_vowel = ["uni30A1", "uni30A2", "uni30A3", "uni30A4", "uni30A5",
                  "uni30A6", "uni30A7", "uni30A8", "uni30A9", "uni30AA"]
Latin_conso = [
    "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z",
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

Latin_Sml = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Latin_weight = [
    0.0787, 0.0156, 0.0268, 0.0389, 0.1267, 0.0256, 0.0187, 0.0573, 0.0707,
    0.0010, 0.0060, 0.0394, 0.0244, 0.0706, 0.0776, 0.0186, 0.0009, 0.0594,
    0.0634, 0.0977, 0.0280, 0.0102, 0.0214, 0.0016, 0.0202, 0.0006]

Greek_Sml = [
    'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ',
    'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']

Greek_Sml_name = [
    "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "uni03BC",
    "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"]

Greek_Cap_name = [
    "Alpha", "Beta", "Gamma", "uni0394", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu",
    "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "uni03A9"]

Greek_weight = [
    0.1285, 0.0055, 0.0174, 0.0136, 0.0930, 0.0049, 0.0385, 0.0152, 0.0957, 0.0302, 0.0213, 0.0427,
    0.0752, 0.0032, 0.1038, 0.0378, 0.0351, 0.0710, 0.0732, 0.0464, 0.0056, 0.0136, 0.0017, 0.0269]

Russia_Sml = ["0x430", "0x431", "0x432", "0x433", "0x434", "0x435", "0x436", "0x437",
              "0x438", "0x439", "0x43a", "0x43b", "0x43c", "0x43d", "0x43e", "0x43f",
              "0x440", "0x441", "0x442", "0x443", "0x444", "0x445", "0x446", "0x447",
              "0x448", "0x449", "0x44a", "0x44b", "0x44c", "0x44d", "0x44e", "0x44f"]

Russia_Sml_name = ["uni0430", "uni0431", "uni0432", "uni0433", "uni0434", "uni0435", "uni0436", "uni0437",
                   "uni0438", "uni0439", "uni043A", "uni043B", "uni043C", "uni043D", "uni043E", "uni043F",
                   "uni0440", "uni0441", "uni0442", "uni0443", "uni0444", "uni0445", "uni0446", "uni0447",
                   "uni0448", "uni0449", "uni044A", "uni044B", "uni044C", "uni044D", "uni044E", "uni044F"]

Russia_Cap = ["0x410", "0x411", "0x412", "0x413", "0x414", "0x415", "0x416", "0x417",
              "0x418", "0x419", "0x41a", "0x41b", "0x41c", "0x41d", "0x41e", "0x41f",
              "0x420", "0x421", "0x422", "0x423", "0x424", "0x425", "0x426", "0x427",
              "0x428", "0x429", "0x42a", "0x42b", "0x42c", "0x42d", "0x42e", "0x42f"]

Russia_weight = [0.0764, 0.0201, 0.0438, 0.0172, 0.0309, 0.0875, 0.0101, 0.0148,
                 0.0709, 0.0121, 0.0330, 0.0496, 0.0317, 0.0678, 0.1118, 0.0247,
                 0.0423, 0.0497, 0.0609, 0.0222, 0.0021, 0.0095, 0.0039, 0.0140,
                 0.0072, 0.0030, 0.0002, 0.0236, 0.0184, 0.0036, 0.0047, 0.0196]

COMMON = ["uni4E00", "uni4E01", "uni4E02", "uni4E03", "uni4E04", "uni4E05",
          "uni4E06", "uni4E07", "uni4E08", "uni4E09", "uni4E0A", "uni4E0B"]


def INIT():
    JP_Hiragana.clear()
    JP_Hiragana.extend((
        "uni3041", "uni3042", "uni3043", "uni3044", "uni3045", "uni3046", "uni3047", "uni3048", "uni3049",
        "uni304A", "uni304B", "uni304C", "uni304D", "uni304E", "uni304F", "uni3050", "uni3051", "uni3052",
        "uni3053", "uni3054", "uni3055", "uni3056", "uni3057", "uni3058", "uni3059", "uni305A", "uni305B",
        "uni305C", "uni305D", "uni305E", "uni305F", "uni3060", "uni3061", "uni3062", "uni3063", "uni3064",
        "uni3065", "uni3066", "uni3067", "uni3068", "uni3069", "uni306A", "uni306B", "uni306C", "uni306D",
        "uni306E", "uni306F", "uni3070", "uni3071", "uni3072", "uni3073", "uni3074", "uni3075", "uni3076",
        "uni3077", "uni3078", "uni3079", "uni307A", "uni307B", "uni307C", "uni307D", "uni307E", "uni307F",
        "uni3080", "uni3081", "uni3082", "uni3083", "uni3084", "uni3085", "uni3086", "uni3087", "uni3088",
        "uni3089", "uni308A", "uni308B", "uni308C", "uni308D", "uni308E", "uni308F", "uni3090", "uni3091",
        "uni3092", "uni3093", "uni3094", "uni309D", "uni309E"))

    JP_Katakana.clear()
    JP_Katakana.extend((
        "uni30AB", "uni30AD", "uni30AF", "uni30B1", "uni30B3", "uni30B5", "uni30B7", "uni30B9", "uni30BB",
        "uni30BD", "uni30BF", "uni30C1", "uni30C6", "uni30C8", "uni30CA", "uni30CB", "uni30CC", "uni30CD",
        "uni30CE", "uni30CF", "uni30D2", "uni30D5", "uni30D8", "uni30DB", "uni30DE", "uni30DF", "uni30E0",
        "uni30E1", "uni30E2", "uni30E4", "uni30E6", "uni30E8", "uni30E9", "uni30EA", "uni30EB", "uni30EC",
        "uni30ED", "uni30EF", "uni30F0", "uni30F1", "uni30F2", "uni30F3"))

    Latin_Cap.clear()
    Latin_Cap.extend((
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'))

    Greek_Cap.clear()
    Greek_Cap.extend((
        'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ',
        'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω'))

    Russia_Cap_name.clear()
    Russia_Cap_name.extend((
        "uni0410", "uni0411", "uni0412", "uni0413", "uni0414", "uni0415", "uni0416", "uni0417",
        "uni0418", "uni0419", "uni041A", "uni041B", "uni041C", "uni041D", "uni041E", "uni041F",
        "uni0420", "uni0421", "uni0422", "uni0423", "uni0424", "uni0425", "uni0426", "uni0427",
        "uni0428", "uni0429", "uni042A", "uni042B", "uni042C", "uni042D", "uni042E", "uni042F"))

    Number.clear()
    Number.extend(("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"))


INIT()
if __name__ == "__main__":
    print(Number)
