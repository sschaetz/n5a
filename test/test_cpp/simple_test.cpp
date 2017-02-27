#define BOOST_TEST_MODULE simple_test

#include <fstream>

#include <boost/test/unit_test.hpp>

#include "generated/pos3d.hpp"

#include <cereal/archives/json.hpp>

BOOST_AUTO_TEST_CASE(simple_cpp_test)
{
    Pos3D p_out;
    {
        p_out.x = 4;
        p_out.y = 1;
        p_out.z = 2;
    }

    Pos3D p_in;
    {
        p_in.x = 50;
        p_in.y = 50;
        p_in.z = 50;
    }

    {
        std::ofstream out("pos3d.json");
        cereal::JSONOutputArchive archive(out);
        archive(::cereal::make_nvp("pos3d", p_out));
    }
    {
        std::ifstream in("pos3d.json");
        cereal::JSONInputArchive archive(in);
        archive(::cereal::make_nvp("pos3d", p_in));
    }

    BOOST_CHECK(p_out.x == p_in.x);
    BOOST_CHECK(p_out.y == p_in.y);
    BOOST_CHECK(p_out.z == p_in.z);
}
