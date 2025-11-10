#ifndef MODULE_NAME
#define MODULE_NAME MyHelloPlugin
#endif

#include <core/core.h>
#include <plugins/plugins.h>

MODULE_NAME_DECLARATION("MyHelloPlugin")

namespace WPEFramework
{
    namespace Plugin
    {
        class HelloPlugin : public PluginHost::IPlugin, public PluginHost::JSONRPC
        {
            public:
            HelloPlugin()
                : PluginHost::JSONRPC()
            {
                Register(_T("SayHello"), &HelloPlugin::SayHello, this);

            }

	    ~HelloPlugin() override
            {
                Unregister(_T("SayHello"));
    	    }


	    virtual const string Initialize(PluginHost::IShell* service) override
            {
                SYSLOG(Logging::Startup, (_T("Initializing TestPlugin")));

                return string();
            }

            virtual void Deinitialize(PluginHost::IShell* service) override
            {
                SYSLOG(Logging::Startup, (_T("Deinitializing TestPlugin")));
            }

            virtual string Information() const override
            {
                return string();
            }

            // JSON-RPC method implementation
            uint32_t SayHello(const JsonObject& parameters, JsonObject& response)
            {
                SYSLOG(Logging::Startup, (_T("SayHello called")));

                string name = parameters.HasLabel("name") ? parameters["name"].String() : "World";

                response["message"] = "Hello " + name + " from TestPlugin";

                return Core::ERROR_NONE; // 0 = success
            }
            
	    //Build QueryInterface implementation, specifying all possible interfaces to be returned.
            BEGIN_INTERFACE_MAP(HelloPlugin)
            INTERFACE_ENTRY(PluginHost::IPlugin)
            INTERFACE_ENTRY(PluginHost::IDispatcher)
            END_INTERFACE_MAP
        };

        static Plugin::Metadata<Plugin::HelloPlugin> metadata(
            // Version (Major, Minor, Patch)
            1, 0, 0,
            // Preconditions
            {},
            // Terminations
            {},
            // Controls
            {}
        );

    }
}


