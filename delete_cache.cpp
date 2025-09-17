#include <filesystem>
#include <iostream>
#include <sstream>

void delete_directory(std::string path){
    try {
        for (const auto& entry : std::filesystem::directory_iterator(path)) {
            try {
                if (std::filesystem::is_directory(entry.path())) {
                    std::filesystem::remove_all(entry.path());
                } else {
                    std::filesystem::remove(entry.path());
                }
                std::cout << "Deleted: " << entry.path() << "\n";
            } catch (const std::exception& e) {
                std::cerr << "Failed to remove: " << entry.path() << "(" << e.what() << ")\n";
            }
        }
    } catch (const std::exception& e) {
        std::cerr << "Error accessing temp folder: " << e.what() << "\n";
    }
}

int main()
{
	std::string modes[] = {std::getenv("TEMP"), R"(C:\Windows\SoftwareDistribution\Download)"};
    std::string path = R"()";
    std::cout << "=========================\n";
    std::cout << "=== Delete Temp Files ===\n";
    std::cout << "=========================\n";
    std::cout << "Press the corresponding number to delete what you want.\n";
    std::cout << "[0] TMP (default)\n[1] System Cache\n";
    unsigned short int option = 0;
    std::string *check_empty = new std::string;
    std::cout << "Enter your choice: ";
	std::getline(std::cin, *check_empty);
	if (check_empty->empty()) {
		delete_directory(modes[option]);
	} else {
		std::istringstream iss(*check_empty);
		if (iss >> option) {
			char remaining_char;
			if (!(iss >> remaining_char)) {
				delete_directory(modes[option]);
			} else {
				std::cout << "Invalid Option, exiting...";
				exit(-1);
			}
		} else {
			std::cout << "Invalid Option, exiting...";
		}
	}
    return 0;
}
