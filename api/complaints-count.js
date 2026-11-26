export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Cache-Control", "s-maxage=1800, stale-while-revalidate=86400");

  try {
    const response = await fetch("https://www.ascionline.in/", {
      headers: {
        "User-Agent": "Mozilla/5.0 (compatible; ASCIWebsiteSync/1.0)",
      },
    });
    if (!response.ok) {
      throw new Error(`Upstream HTTP ${response.status}`);
    }
    const html = await response.text();
    const match = html.match(
      /complaints-res[\s\S]*?<span[^>]*class="[^"]*counter[^"]*"[^>]*>\s*([\d,]+)/i
    );
    if (!match) {
      throw new Error("Counter element not found in upstream HTML");
    }
    const numeric = parseInt(match[1].replace(/,/g, ""), 10);
    return res.status(200).json({
      count: numeric,
      formatted: numeric.toLocaleString("en-US"),
      source: "live",
    });
  } catch (err) {
    return res.status(200).json({
      count: 92143,
      formatted: "92,143",
      source: "fallback",
    });
  }
}
