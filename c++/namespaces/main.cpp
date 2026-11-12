#include <iostream>
namespace audio { void init() { std::cout << "audio init\n"; } int volume = 5; }
namespace video { void init() { std::cout << "video init\n"; } int volume = 9; }
int volume = 1;                       // global one
int main() {
    audio::init();
    video::init();
    std::cout << "audio::volume=" << audio::volume
              << " video::volume=" << video::volume
              << " ::volume=" << ::volume << "\n";
    using namespace audio;            // pull audio's names in
    init();                           // now means audio::init
    return 0;
}
