import java.util.List;
import java.util.ArrayList;

public class SimplifyPath {
	public String simplifyPath(String path) {
		List<String> ss = new ArrayList<String>();
		String cmd;

		for (String x: path.split("/")) {
			switch (x) {
				case "..":
					if (ss.size() == 0)
						continue;
					else
						ss.remove(ss.size()-1);
					break;
				case ".":
					break;
				case "":
					break;
				default:
					ss.add(x);
					break;
			}
		}

		// reverse
		StringBuilder sbret = new StringBuilder();
		for (String s: ss) {
			sbret.append(s);
			if (!s.equals(ss.get(ss.size()-1)))
			    sbret.append("/"); // no '/' at the end
		}

		return "/"+sbret.toString();
	}

	public static void
	main(String[] args) {
		if (args.length <= 0) {
			return;
		}

		String path = args[0];
		SimplifyPath sp = new SimplifyPath();
		System.out.println(sp.simplifyPath(path));
	}
}