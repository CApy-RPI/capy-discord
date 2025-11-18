ARG python_version=3.13-slim
ARG uv_version=0.9.10

FROM python:${python_version} AS builder
COPY --from=ghcr.io/astral-sh/uv:${uv_version} /uv /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /build

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-dev

# -------------------------------------------------------------------------------

FROM python:${python_version}

ARG git_sha="development"
ENV GIT_SHA=$git_sha

COPY --from=builder /build /build
ENV PATH="/build/.venv/bin:$PATH"

WORKDIR /app
COPY bot/ ./bot/

ENTRYPOINT ["python"]
CMD ["-m", "bot.main"]
