file(GLOB_RECURSE srcs RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *)
list(REMOVE_ITEM srcs CMakeLists.txt test legacy)
install(FILES ${srcs} DESTINATION lib/vera++/profiles)
