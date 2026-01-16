import fs from "fs/promises";
import path from "path";
import sharp from "sharp";

const INPUT_DIR = path.resolve("images", "original");
const OUTPUT_DIR = path.resolve("images", "avif");
const INPUT_EXTS = new Set([".jpg", ".jpeg", ".png", ".webp"]);

async function ensureDir(dirPath: string): Promise<void> {
  await fs.mkdir(dirPath, { recursive: true });
}

async function fileExists(filePath: string): Promise<boolean> {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

async function convertOne(inputPath: string, outputPath: string): Promise<void> {
  try {
    if (await fileExists(outputPath)) {
      return;
    }

    await sharp(inputPath)
      .avif({
        quality: 40,
        effort: 5,
        chromaSubsampling: "4:2:0",
      })
      .toFile(outputPath);
  } catch (error) {
    console.warn(`Skip on error: ${inputPath}`, error);
  }
}

async function main(): Promise<void> {
  await ensureDir(OUTPUT_DIR);

  let entries: string[];
  try {
    entries = await fs.readdir(INPUT_DIR);
  } catch (error) {
    console.error(`Failed to read input dir: ${INPUT_DIR}`, error);
    return;
  }

  const tasks: Promise<void>[] = [];

  for (const entry of entries) {
    const inputPath = path.join(INPUT_DIR, entry);
    const stat = await fs.stat(inputPath).catch(() => null);
    if (!stat || !stat.isFile()) {
      continue;
    }

    const extOriginal = path.extname(entry);
    const extLower = extOriginal.toLowerCase();
    if (!INPUT_EXTS.has(extLower)) {
      continue;
    }

    const baseName = path.basename(entry, extOriginal);
    const outputPath = path.join(OUTPUT_DIR, `${baseName}.avif`);
    tasks.push(convertOne(inputPath, outputPath));
  }

  await Promise.all(tasks);
}

main().catch((error) => {
  console.error("Unexpected error:", error);
});
