from fastmcp import FastMCP

mcp = FastMCP(name="TestRemoteMCPServer")

@mcp.tool()
def hello(name: str) -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()