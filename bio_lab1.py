import matplotlib.pyplot as plt
from collections import Counter

def get_kmer_frequencies(sequence, k):

    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    return Counter(kmers)

def plot_frequencies(freq_dict, title, filename):

    sorted_items = sorted(freq_dict.items())
    labels = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]
    
    plt.figure(figsize=(10, 5))
    bars = plt.bar(labels, counts, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel('Sequence Combination')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, int(yval), ha='center', va='bottom')
        
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


S = "ATCGACGCTAACGTA"


freq_1 = get_kmer_frequencies(S, 1)
print(f"1-letter frequencies: {dict(freq_1)}")
plot_frequencies(freq_1, f'1-Letter Frequencies ({S})', 'freq_1.png')


freq_2 = get_kmer_frequencies(S, 2)
print(f"2-letter frequencies: {dict(freq_2)}")
plot_frequencies(freq_2, f'2-Letter Frequencies ({S})', 'freq_2.png')


freq_3 = get_kmer_frequencies(S, 3)
print(f"3-letter frequencies: {dict(freq_3)}")
plot_frequencies(freq_3, f'3-Letter Frequencies ({S})', 'freq_3.png')