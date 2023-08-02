import { render, screen } from "./helpers/test-utils";
import App from "./App";

test("renders Welcome to weTalk text", () => {
  render(<App />);
  const linkElement = screen.getByText(/Welcome to weTalk!/i);
  expect(linkElement).toBeInTheDocument();
});
