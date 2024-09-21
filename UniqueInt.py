import os

class UniqueInt:
    @staticmethod
    def process_file(input_file_path, output_file_path):
        seen = set()  # To store unique integers
        try:
            # Open input file for reading and output file for writing
            with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
                for line in infile:
                    line = line.strip()  # Remove leading/trailing whitespaces
                    if line:  # Check if the line is not empty
                        try:
                            num = int(line)  # Try to convert the line to an integer
                            # Print the number being processed
                            print("Processing number: {}".format(num))
                            
                            # Only process if the number is within the valid range
                            if -1023 <= num <= 1023:  # Ensure num is in the valid range
                                if num not in seen:  # If the integer is not already in the set
                                    seen.add(num)  # Add it to the set
                                    outfile.write("{}\n".format(num))  # Write the unique integer to the output file
                                    print("Writing number: {}".format(num))  # Debug statement
                        except ValueError:
                            # Print a message if the line is not a valid integer
                            print("Skipping non-integer value: {}".format(line))
        except FileNotFoundError:
            # Print a message if the input file is not found
            print("Error: File {} not found.".format(input_file_path))

    @staticmethod
    def process_directory(input_dir, output_dir):
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Process each file in the input directory
        for filename in os.listdir(input_dir):
            if filename.endswith(".txt"):  # Only process .txt files
                input_file_path = os.path.join(input_dir, filename)
                output_file_path = os.path.join(output_dir, "results_{}".format(filename))
                UniqueInt.process_file(input_file_path, output_file_path)
                # Print a message after processing each file
                print("Processed {} and saved results to {}".format(filename, output_file_path))

if __name__ == "__main__":
    input_dir = 'input'
    output_dir = 'results'

    # Process all .txt files in the input directory
    UniqueInt.process_directory(input_dir, output_dir)

