CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

# Find Boost libraries.
OPTION(BOOST_TEST_DYN_LINK
       "Link tests against dynamic version of boost unittest library" ON)
IF (WIN32)
        SET(Boost_USE_STATIC_LIBS ON)
ELSE ()
        IF (BOOST_TEST_DYN_LINK)
                ADD_DEFINITIONS(-DBOOST_TEST_DYN_LINK)
        ENDIF ()
ENDIF()
FIND_PACKAGE(Boost COMPONENTS unit_test_framework)


# Compiler and linker flags
ADD_COMPILE_OPTIONS(-std=c++0x -g -O3)
IF (WIN32)
        ADD_COMPILE_OPTIONS(/EHsc)
        ADD_COMPILE_OPTIONS(/W3)
ELSE()
        # Prevent VS from spewing lots of warnings.
        ADD_COMPILE_OPTIONS(-Wall)
        ADD_COMPILE_OPTIONS(-Werror)
ENDIF()

INCLUDE_DIRECTORIES("../external/ceral=1.2.2/")

ENABLE_TESTING()

ADD_EXECUTABLE(simple_test simple_test.cpp)
TARGET_LINK_LIBRARIES(simple_test ${Boost_UNIT_TEST_FRAMEWORK_LIBRARY})
ADD_TEST(simple_test, simple_test)