import os

class UniqueInt:
    @staticmethod
    def process_file(input_file_path, output_file_path):
        seen = set()  # To store unique integers
        try:
            with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
                for line in infile:
                    line = line.strip()  # Remove whitespaces
                    if line:  # Skip empty lines
                        try:
                            num = int(line)  # Convert line to an integer
                            if num not in seen:  # Check if already seen
                                seen.add(num)
                                outfile.write("{}\n".format(num))  # Write unique integer to the output file
                        except ValueError:
                            print("Skipping non-integer value: {}".format(line))
        except FileNotFoundError:
            print(f"Error: File {input_file_path} not found.")

    @staticmethod
    def process_directory(input_dir, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for filename in os.listdir(input_dir):
            if filename.endswith(".txt"):  # Process only .txt files
                input_file_path = os.path.join(input_dir, filename)
                output_file_path = os.path.join(output_dir, f"results_{filename}")
                UniqueInt.process_file(input_file_path, output_file_path)
                print(f"Processed {filename} and saved results to {output_file_path}")

if __name__ == "__main__":
    input_dir = 'input'
    output_dir = 'results'

    UniqueInt.process_directory(input_dir, output_dir)
