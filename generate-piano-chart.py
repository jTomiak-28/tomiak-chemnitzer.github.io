import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from colorsys import rgb_to_hls, hls_to_rgb

# --- Load data ---
df = pd.read_csv("full-mapping.csv")

# --- Convert note names to MIDI numbers ---
note_map = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def note_to_midi(note):
    name = note[:-1]
    octave = int(note[-1])
    return 12*(octave + 1) + note_map[name]

df["midi"] = df["Note"].apply(note_to_midi)

# --- Determine coverage by side and button count ---
coverage = (
    df.groupby("midi")
      .agg(Sides=("Side", lambda x: set(x)),
           n_buttons=("Button", "nunique"))
      .reset_index()
)

# --- Normalize button counts (brightness scale) ---
max_buttons = 5  # known max from your data
coverage["intensity"] = coverage["n_buttons"] / max_buttons

# --- Assign base color by side coverage ---
def key_color(sides):
    if "left" in sides and "right" in sides:
        return "green"
    elif "left" in sides:
        return "gold"
    elif "right" in sides:
        return "dodgerblue"
    else:
        return "lightgray"

coverage["base_color"] = coverage["Sides"].apply(key_color)

# --- Apply brightness scaling ---
def adjust_brightness(color, factor):
    r, g, b = mcolors.to_rgb(color)
    h, l, s = rgb_to_hls(r, g, b)
    gamma = 1.5
    factor = factor ** gamma
    min_l, max_l = 0.3, 0.9
    l_new = min_l + factor * (max_l - min_l)
    return hls_to_rgb(h, l_new, s)

coverage["color"] = [
    adjust_brightness(c, i) for c, i in zip(coverage["base_color"], coverage["intensity"])
]

# Draw keyboard
fig, ax = plt.subplots(figsize=(16, 3))

# --- Precompute note names and helpers ---
note_names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def midi_to_note_name(midi):
    return note_names[midi % 12], midi // 12 - 1

key_width, key_height = 1.0, 1.0
black_key_width, black_key_height = 0.6, 0.6
start, end = coverage["midi"].min() - 1, coverage["midi"].max() + 1
white_notes = [0,2,4,5,7,9,11]
midi_to_x = {}
x = 0

# --- 1. Draw white keys base ---
for midi in range(start, end + 1):
    note_name, _ = midi_to_note_name(midi)
    if '#' not in note_name:
        ax.add_patch(Rectangle((x, 0), key_width, key_height,
                               facecolor='white', edgecolor='k',
                               linewidth=1.0, zorder=1))
        midi_to_x[midi] = x
        x += 1

# --- 2. Draw white key colored overlays (brightness-scaled) ---
for _, row in coverage.iterrows():
    midi = row["midi"]
    if midi in midi_to_x and '#' not in midi_to_note_name(midi)[0]:
        color = row["color"]
        ax.add_patch(Rectangle((midi_to_x[midi], 0),
                               key_width, key_height,
                               facecolor=color,
                               edgecolor='k', linewidth=1.0,
                               alpha=0.9, zorder=2))

# --- Label the C keys with octave numbers ---
for midi, xpos in midi_to_x.items():
    note_name, octave = midi_to_note_name(midi)
    if note_name == 'C':
        label = f"C{octave}"
        ax.text(xpos + 0.5, -0.08, label,
                ha='center', va='top',
                fontsize=8, fontweight='bold', color='black', zorder=10)

# --- 3. Draw black keys (on top of whites) ---
for midi in range(start, end + 1):
    note_name, _ = midi_to_note_name(midi)
    if '#' in note_name:
        prev_white = midi - 1
        if prev_white in midi_to_x:
            bx = midi_to_x[prev_white] + 0.7
            ax.add_patch(Rectangle((bx, 0.4),
                                   black_key_width, black_key_height,
                                   facecolor='black', edgecolor='k',
                                   linewidth=1.0, zorder=5))
            midi_to_x[midi] = bx

# --- 4. Optional colored overlays for black keys (if desired) ---
for _, row in coverage.iterrows():
    midi = row["midi"]
    if midi in midi_to_x and '#' in midi_to_note_name(midi)[0]:
        color = row["color"]
        bx = midi_to_x[midi]
        ax.add_patch(Rectangle((bx, 0.4),
                               black_key_width, black_key_height,
                               facecolor=color,
                               edgecolor='k', linewidth=1.0,
                               alpha=0.9, zorder=6))

# --- 5. Final styling ---
ax.set_xlim(-1, x)
ax.set_ylim(0, 1.1)
ax.axis('off')
plt.title("Chemnitzer Keyboard Coverage", fontsize=12)

# --- Build legend showing button count shading ---
legend_colors = []
for n in range(1, 6):  # 1–5 buttons
    intensity = n / 5
    color = adjust_brightness('gray', intensity)  # neutral example color
    legend_colors.append(mpatches.Patch(facecolor=color,
                                        edgecolor='k',
                                        label=f"{n} button{'s' if n>1 else ''}"))

legend_patches = [
    mpatches.Patch(color='gold', label='Left Hand'),
    mpatches.Patch(color='dodgerblue', label='Right Hand'),
    mpatches.Patch(color='green', label='Both Hands')
]

# --- Place legends outside the keyboard area (left side) ---

# Hand Side legend (top-left outside)
first_legend = plt.legend(
    handles=legend_patches,
    title="Hand Side",
    loc='upper left',
    bbox_to_anchor=(-0.20, 1.0),   # (x, y) relative to axes
    frameon=True
)
ax.add_artist(first_legend)

# Brightness legend (below the first one, still off to the left)
plt.legend(
    handles=legend_colors,
    title="Number of Buttons (Brightness)",
    loc='upper left',
    bbox_to_anchor=(-0.20, 0.5),   # adjust y to control spacing
    frameon=True
)

# Adjust figure layout so the legends fit
plt.subplots_adjust(left=0.25, right=0.98)  # make room on left for legends
plt.show()