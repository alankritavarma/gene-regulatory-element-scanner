# Simple Python code for finding promoter-related motifs

MOTIFS = {
    "TATA Box": "TATA",
    "CAAT Box": "CAAT",
    "GC Box (simplified)": "GC"
}


def clean_sequence(sequence):
    """Make the sequence uppercase and remove spaces/new lines."""
    return "".join(sequence.upper().split())


def is_valid(sequence):
    """Check that the sequence contains only A, T, G and C."""
    return len(sequence) > 0 and all(base in "ATGC" for base in sequence)


def find_positions(sequence, motif):
    """Return the start positions of a motif (counting from 1)."""
    positions = []

    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i + len(motif)] == motif:
            positions.append(i + 1)

    return positions


def scan_sequence(sequence):
    """Find each motif and return its positions."""
    results = {}

    for name, motif in MOTIFS.items():
        positions = find_positions(sequence, motif)
        results[name] = positions

    return results


def get_gc_content(sequence):
    """Calculate the percentage of G and C bases."""
    if len(sequence) == 0:
        return 0

    gc_count = sequence.count("G") + sequence.count("C")
    return round((gc_count / len(sequence)) * 100, 2)
