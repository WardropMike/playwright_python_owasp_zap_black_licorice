# How to run this script
# At the terminal in the project root run the following command
# python3 /Users/temp/Documents/Coding/the_python_proj/black_licorice/app/src/extract_grid.py
import requests
from bs4 import BeautifulSoup

def extract_and_render_grid(url, output_file="grid_output.txt"):
    try:
        # Fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table, dynamically identified by its structure, not the class name
        table = soup.find("table")
        if not table:
            print("Table not found. Check the structure.")
            return

        # Find all rows in the table
        rows = table.find_all("tr")
        if not rows:
            print("No rows found in the table. Check the structure.")
            return

        coordinates = []

        # Process each row to extract the coordinates and characters
        for row in rows:
            cells = row.find_all("td")

            # Skip the header row that contains labels (x-coordinate, Character, y-coordinate)
            if len(cells) < 3 or 'x-coordinate' in [cell.get_text(strip=True) for cell in cells]:
                continue

            try:
                # Extract data based on position rather than class names
                x_cell = cells[0].find("span")
                char_cell = cells[1].find("span")
                y_cell = cells[2].find("span")

                if x_cell and char_cell and y_cell:
                    x_coordinate = int(x_cell.text.strip())
                    character = char_cell.text.strip()
                    y_coordinate = int(y_cell.text.strip())
                    coordinates.append((x_coordinate, y_coordinate, character))
                else:
                    print(f"Skipping row with missing data please: {row}")
            except (AttributeError, ValueError) as e:
                print(f"Skipping row due to invalid data please: {e}")
                continue

        if not coordinates:
            print("No valid data extracted. Check the structure or class names.")
            return

        # Determine the grid size based on max x and y coordinates
        x_max = max(coord[0] for coord in coordinates)
        y_max = max(coord[1] for coord in coordinates)

        # Initialize the grid with spaces
        grid = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        # Place the characters in the grid
        for x, y, char in coordinates:
            grid[y][x] = char

        # Print the secret message in a fixed-width font
        print("\nSecret Message:")
        for row in grid:
            print("".join(row))  # This will print in a fixed-width format in iTerm

        # Save the output to a file
        with open(output_file, "w") as file:
            for row in grid:
                file.write("".join(row) + "\n")

        print(f"\nGrid output saved to {output_file}. Open with a fixed-width font editor.")

    except requests.RequestException as e:
        print(f"Error fetching the URL address: {e}")
    except Exception as e:
        print(f"Error processing the data: {e}")

# Function to call the extraction and rendering
def print_secret_message(url):
    extract_and_render_grid(url)

# Replace this with your URL
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
print_secret_message(url)
